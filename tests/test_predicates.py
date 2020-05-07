import unittest
from predicates import Equals, LessThan, LessThanEqual, GreaterThan, GreaterThanEqual


class PredicatesTestCase(unittest.TestCase):

    def test_equals_predicate(self):
        eq_hello = Equals("hello")
        eq_5 = Equals(5)

        self.assertTrue(eq_hello.evaluate("hello"))
        self.assertFalse(eq_hello.evaluate("bye"))
        self.assertFalse(eq_hello.evaluate(False))
        self.assertFalse(eq_hello.evaluate(5))
        self.assertFalse(eq_hello.evaluate(None))

        self.assertTrue(eq_5.evaluate(5))
        self.assertFalse(eq_hello.evaluate(7))
        self.assertFalse(eq_hello.evaluate("5"))
        self.assertFalse(eq_hello.evaluate(False))
        self.assertFalse(eq_hello.evaluate(None))

    def test_less_than_predicate(self):
        lt_hello = LessThan("hello")
        lt_5 = LessThan(5)

        self.assertTrue(lt_hello.evaluate("abc"))
        self.assertFalse(lt_hello.evaluate("zebra"))

        self.assertTrue(lt_5.evaluate(1))
        self.assertFalse(lt_5.evaluate(10))

    def test_less_than_equals_predicate(self):
        lte_hello = LessThanEqual("hello")
        lte_5 = LessThanEqual(5)

        self.assertTrue(lte_hello.evaluate("abc"))
        self.assertTrue(lte_hello.evaluate("hello"))
        self.assertFalse(lte_hello.evaluate("zebra"))

        self.assertTrue(lte_5.evaluate(1))
        self.assertTrue(lte_5.evaluate(5))
        self.assertFalse(lte_5.evaluate(10))

    def test_greater_than_predicate(self):
        gt_hello = GreaterThan("hello")
        gt_5 = GreaterThan(5)

        self.assertTrue(gt_hello.evaluate("zebra"))
        self.assertFalse(gt_hello.evaluate("abc"))

        self.assertTrue(gt_5.evaluate(10))
        self.assertFalse(gt_5.evaluate(1))

    def test_greater_than_equals_predicate(self):
        gte_hello = GreaterThanEqual("hello")
        gte_5 = GreaterThanEqual(5)

        self.assertTrue(gte_hello.evaluate("zebra"))
        self.assertTrue(gte_hello.evaluate("hello"))
        self.assertFalse(gte_hello.evaluate("abc"))

        self.assertTrue(gte_5.evaluate(10))
        self.assertTrue(gte_5.evaluate(5))
        self.assertFalse(gte_5.evaluate(1))