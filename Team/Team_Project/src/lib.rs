use std::{collections::HashMap};
use pyo3::{prelude::*, types::PyByteArray};

/// Formats the sum of two numbers as string.
/// /// the pyfuntion macro indicates that it can be called from python
/// the -> is the type we get in python 
#[pyfunction] 
fn count_words(s: String) -> Py<PyAny> {
    let mut hm = HashMap::new();
    for sub_str in s.split(' ') {
        let count = hm
            .entry(sub_str)
            .or_insert(0);
        *count += 1;
    }
    
    return Python::with_gil(|py| {
        hm.to_object(py)
    });
}
/// byte array type, used to convert bytes into vectors of u8
/*
Vectors are re-sizable arrays. Like slices, their size is not known at compile time,
but they can grow or shrink at any time. A vector is represented using 3 parameters:
pointer to the data
length
capacity
The capacity indicates how much memory is reserved for the vector. The vector
can grow as long as the length is smaller than the capacity. When this threshold 
 needs to be surpassed, the vector is reallocated with a larger capacity.
 */
///pyo3 automaticaly converts byte objects to u8
#[pyfunction]
fn first_byte(a: Vec<u8>) -> u8 { 
    a[0]
}
#[pyfunction] /// this gets converted to a native rust type
fn last_byte(a:&PyByteArray) -> u8 {
     let v:Vec<u8> = a.extract().unwrap_or_default();
     v[v.len() - 1]
    }
#[pyfunction] 
fn test(){
    println!("This is working")
}
#[pyfunction]
fn cal(){
    let y = 2 * 2; 
    println!(" The value is :{y}")
}


/// A Python module implemented in Rust.
/// This funtion is used to impliment the code to python
/// add the funtions here to  impliment it in the python side. 
#[pymodule]
fn Team_Project(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count_words, m)?)?;
    m.add_function(wrap_pyfunction!(first_byte,m)?)?;
    m.add_function(wrap_pyfunction!(last_byte,m)?)?;
    m.add_function(wrap_pyfunction!(test,m)?)?;
    m.add_function(wrap_pyfunction!(cal,m)?)?;  
    Ok(())
}