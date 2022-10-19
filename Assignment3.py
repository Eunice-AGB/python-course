import cmath
a = float(input("Input the value of a: "))
b = float(input("Input the value of b: "))
c = float(input("Input the value of c: "))
y = (b**2) - (4 * a * c)
# x = cmath.sqrt(y)
# x = math.sqrt(b**2 - (4 * a * c))
# z = (-b + x) / 2 * a
minusSol = ((-b-cmath.sqrt(y))/(2*a))
plusSol = ((-b+cmath.sqrt(y))/(2*a))
# print("The answer to the solution are: ".format(minusSol,plusSol))
print(minusSol, plusSol)
