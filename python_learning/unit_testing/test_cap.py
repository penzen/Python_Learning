import unittest # build in funtion 
import cap

class test_Class(unittest.TestCase):  # inherite from unittest 

    def test_oneword(self): # this is a test 
        text = "python"
        result = cap.gunit(text) # from the cap class 
        self.assertEqual(result,'Python')
        # self.assertEqual() basically is == saying that the result has to equal to this

    def test_multiple(self): 
        text = " Monty Python"
        result = cap.gunit(text) # from the cap class
        self.assertEqual(result, " Monty Python")

# if __name__ == '__main__': need more inforatiom on this 

    
if __name__ == '__main__': # have to use this for unit testing 
    unittest.main()
