
# def wise():
#     new = 7
#     print(new+12)
#     print("I am Wisdom")

# wise()

# Function with positional arguments
# def wise(weight, height):
#     bmi = (height ** 2)/weight
    # print(bmi)
    # return bmi
# w = int(input("Weight: "))
# h = int(input("Height: "))
# my_bmi = wise(w, h)
# print(my_bmi)

# my_bmi = wise(20, 40)
# print(my_bmi)

# Functions with keywords argument
# def BMI(weight=12, height = 15):
#     return(height ** 2)/weight
# var2 = BMI(60, 17)
# print(var2)

# Functions with variable length arguments
# def Result(*args):
#     print(args)
#     Result("Anything", "Dapo", 2, 46, 99, "boy")

# '''Functions with variable length keywords arguments'''
def myFunc(**kwargs):
    print(kwargs)
    # print(kwargs['age'])
    print(kwargs['sex'])

myFunc(age=5, sex="male", level="uni", name="Peter")
