import numbers


class Function:
    """func"""
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        # Check type
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        # Report
        if debug is True:
            print(result)
            # Go home
        return result


class Operator:
    """fire regnereglene"""
    def __init__(self, func, strength):
        self.func = func
        self.strength = strength

    def execute(self, element1, element2, debug=False):
        """# Check type"""
        if not isinstance(element1, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        if not isinstance(element2, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element1, element2)
        # Report
        if debug is True:
            print(result)
            # Go home
        return result


"""exponential_func = Function(numpy.exp)
sin_func = Function(numpy.sin)
print(exponential_func.execute(sin_func.execute(0)))

add_op = Operator(numpy.add, 0)
multiply_op = Operator(numpy.multiply, 1)
print(add_op.execute(1, multiply_op.execute(2, 3)))"""