# Q-69
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# Q-70
# marks = int(input("Enter marks: "))
# if marks >= 40:
#     if marks >= 90:
#         print("A")
#     elif marks >= 75:
#         print("B")
# else:
#     print("Fail")
# The code is not Working because there is an error of range in line-11 and else is not present after nested if and elif  

# Correct code
# marks = int(input("Enter marks: "))
# if marks > 30:
#     if marks >= 90:
#         print("A")
#     elif marks >= 75:
#         print("B")
#     else:
#         print("Pass")
# else:
#     print("Fail")