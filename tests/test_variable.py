import unittest
from variable import Variable


class VariableTestCase(unittest.TestCase):

    def test_compare_variable(self):
        var_1 = Variable("Variable 1", "string")
        var_2 = Variable("Variable 2", "string")
        var_3 = Variable("Variable 1", "string")
        var_4 = Variable("Variable 1", 1)

        self.assertTrue(var_1 == var_1)
        self.assertTrue(var_1 == var_2)
        self.assertTrue(var_1 == var_3)
        self.assertFalse(var_1 == var_4)
