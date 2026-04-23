import unittest
import codeCalc
import pytest

class Calculator(unittest.TestCase):
    def calculate(self, operation, a, b=None):
        """
        operation: 'add', 'subtract', 'multiply', 'divide', 'sqrt'
        """
        raise NotImplementedError()
    
    def test_addition(self):
        result = codeCalc.addition(3,6)
        self.assertEqual(result,9,"Addition Test Failed")
    
    def test_subtraction(self):
        result = codeCalc.sub(3,6)
        self.assertEqual(result,-3,"Subtraction Test Failed")
    
    def test_mult(self):
        result = codeCalc.mult(3,6)
        self.assertEqual(result,18,"Multiplication Test Failed")
    
    def test_division(self):
        result = codeCalc.div(3,6)
        self.assertEqual(result,.5,"Division Test Failed")
        
    def test_int_division(self):
        result = codeCalc.intdiv(6,3)
        self.assertEqual(result,2,"Int Division Test Failed")
        
    def test_addition_operand(self):
        with self.assertRaises(TypeError):
            codeCalc.addition(5)
    def test_sub_operand(self):
        with self.assertRaises(TypeError):
            codeCalc.sub(5)
    def test_mult_operand(self):
        with self.assertRaises(TypeError):
            codeCalc.mult(5)
    def test_div_operand(self):
        with self.assertRaises(TypeError):
            codeCalc.div(5)
    def test_int_div_operand(self):
        with self.assertRaises(TypeError):
            codeCalc.intdiv(5)
            
    def test_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
            codeCalc.div(10, 0)

    def test_invalid_type_operation():
        with pytest.raises(TypeError):
            codeCalc.div(10, "2")  # Cannot divide int by str

    def test_math_domain_error():
        with pytest.raises(ValueError):
            codeCalc.sqrt(-1)
    
        
    
if __name__ == "__main__":
    unittest.main()