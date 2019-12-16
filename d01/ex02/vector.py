class Vector:
    
    def __init__(self, param):
        try:
            assert isinstance(param, list) or isinstance(param, int) or isinstance(param, tuple)
            if isinstance(param, list):
                test = [el for el in param if not isinstance(el, float) and not isinstance(el, int)]
                assert len(test) == 0
                self.values = param
                self.length = len(param)
            elif isinstance(param, int):
                self.values = [x for x in range(param)]
                self.length = param
            else:
                self.values = [x for x in range(param[0], param[1])]
                self.length = param[1] - param[0]
        except (ValueError, AssertionError):
            print("ERROR VECTOR")

    
    def __add__(self, other):
        try:
            assert (isinstance(other, Vector) and self.length == other.length) \
                or  (isinstance(other, list) and self.length == len(other))
            if isinstance(other, list):
                other = Vector(other)
            values = [self.values[i] + other.values[i] for i in range(self.length)]
            return Vector(values)
        except (ValueError, AssertionError):
            print("ERROR VECTOR ADDITION")
            #return (None)


    def __radd__(self, other):
        return self.__add__(other)
    

    def __sub__(self, other):
        try:
            assert (isinstance(other, Vector) and self.length == other.length) \
                or  (isinstance(other, list) and self.length == len(other))
            if isinstance(other, list):
                other = Vector(other)
            values = [self.values[i] - other.values[i] for i in range(self.length)]
            return Vector(values)
        except (ValueError, AssertionError):
            print("ERROR VECTOR ADDITION")


    def __rsub__(self, other):
        return self.__sub__(other)
    

    def __truediv__(self, other):
        try:
            assert isinstance(other, int) or isinstance(other, float)
            assert other != 0
            values = [self.values[i] / other  for i in range(self.length)]
            return Vector(values)
        except (ValueError, AssertionError, ZeroDivisionError):
            print("ERROR VECTOR DIVISION")
            return (None)

    
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __mul__(self, other):
        try:
            assert isinstance(other, Vector) or isinstance(other, int) or isinstance(other, float) or isinstance(other, list)
            if isinstance(other, list):
                other = Vector(other)
            if isinstance(other, Vector):
                assert self.length == other.length 
                values = [self.values[i] * other.values[i] for i in range(self.length)]
                result = 0
                for value in values:
                    result += value 
            else:
                values = [self.values[i] * other for i in range(self.length)]
                result = Vector(values)
            return result
        except (ValueError, AssertionError):
            print("ERROR VECTOR MULTIPLICATION")
            return (None)


    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __str__(self):
        return ("values = " + str(self.values) + " | length = " + str(self.length))

    def __repr__(self):
        print("VECTOR(values{}, length={})".format(self.values, self.length))


    


