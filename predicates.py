"""
Predicates Module
Contains boolean-valued function
"""
from abc import abstractmethod


class Predicate:
    """
    Predicate Class
    Defines the abstract method validate.
    """
    _operator: str
    _operand: object

    def __init__(self, operand: object):
        self._operator = None
        self._operand = operand

    def __str__(self):
        return "{} {}".format(self._operator, self._operand)

    @abstractmethod
    def evaluate(self, operand: object) -> bool:
        """
        Abstract evaluate-method
        Evaluates passed operand against own operand
        :param operand: operand to evaluate
        :return: boolean
        """
        pass

    def _same_type(self, operand: object):
        return isinstance(operand, type(self._operand))


class Equals(Predicate):
    """
    Equals Predicate
    Evaluates operand1 == operand2
    """

    def __init__(self, operand: object):
        super().__init__(operand)
        self._operator = "=="

    def evaluate(self, operand: object):
        return self._same_type(operand) and operand == self._operand


class LessThan(Predicate):
    """
    Less Than Predicate
    Evaluates operand1 < operand2
    """

    def __init__(self, operand: object):
        super().__init__(operand)
        self._operator = "<"

    def evaluate(self, operand: object):
        return self._same_type(operand) and operand < self._operand


class LessThanEqual(Predicate):
    """
    Less Than Equal Predicate
    Evaluates operand1 <= operand2
    """

    def __init__(self, operand: object):
        super().__init__(operand)
        self._operator = "<="

    def evaluate(self, operand: object):
        return self._same_type(operand) and operand <= self._operand


class GreaterThan(Predicate):
    """
    Greater Than Predicate
    Evaluates operand1 > operand2
    """

    def __init__(self, operand: object):
        super().__init__(operand)
        self._operator = ">"

    def evaluate(self, operand: object):
        return self._same_type(operand) and operand > self._operand


class GreaterThanEqual(Predicate):
    """
    Greater Than Equal Predicate
    Evaluates operand1 >= operand2
    """

    def __init__(self, operand: object):
        super().__init__(operand)
        self._operator = ">="

    def evaluate(self, operand: object):
        return self._same_type(operand) and operand >= self._operand