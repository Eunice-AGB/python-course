# If-else conditional statement
# var1 = 18
# age = input("How old are you? ")
# age = int(age)
# if age >= var1:
#     print("You're screwed bro. ")
# else:
#     print("Such a child!")

# if-else-if conditional statement
grade = input("What was your grade? ")
if grade or grade.lower() == "A":
    print(f'Your grade is {5.0}')
elif grade or grade.lower() == "B":
    print(f'Your grade is {4.0}')
elif grade or grade.lower() == "C":
    print(f'Your grade is {3.0}')
elif grade or grade.lower() == "D":
    print(f'Your grade is{2.0}')
elif grade or grade.lower() == "F":
    print(f'Your grade is {0.0}')
else:
    print("You failed!")
