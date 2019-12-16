from vector import Vector

v = Vector([0.0, 1.0, 2.0, 3.0])
print(v)
v1 = Vector(5)
print(v1)
v2 = Vector((5,10))
print(v2)

## ADDITION ##
print(v + v1)
print(v + 5)
print(v1 + v2)
print(["HELLO",2,3,4,5] + v1)
print(v1 + [1,2,3,4,5])

## SUBSTRACTION ##
print(v - v1)
print(v - 5)
print(v1 - v2)
print([1,2,3,4,5] - v1)
print(v1 - [1,2,3,4,5])

## MULTIPLICATION ##
print(v * v1)
print(v * 5)
print(5 * v)
print(v1 * v2)
print([1,2,3,4,5] * v1)
print(v1 * [1,2,3,4,5])

## Division ##
print(v.__truediv__(5))
print(v.__truediv__(0))