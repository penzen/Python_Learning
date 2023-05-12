use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// calling python funtions in rust 

#[pyfunction(pass_module)]
fn pyfunction_with_module(module: &PyModule) -> PyResult<&str> {
    module.name()
}

#[pymodule]
fn module_with_fn(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pyfunction_with_module, m)?)
}

fn main (){
    println!("Hello moron ");
}