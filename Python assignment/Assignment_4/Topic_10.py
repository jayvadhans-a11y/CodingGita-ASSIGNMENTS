# Q-71
# marks = 85
# if marks >= 40:
#     print("Pass")
# elif marks >= 75:
#     print("Very Good")
# else:
#     print("Fail")
#Explaination:Because if statement already become true so code will stop and not go further

# Q-72
# marks = 85
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")
# Because python check the if elif else condition as soon as it find the answer and after finding the answer it did not go further more hence by change the order answer also change

# Q-73
# age = 20
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry Allowed")
#     else:
#         print("ID Required")
# else:
#     print("Underage")
# Entry Allowed

# age = 20
# has_id = False
# ID Required

# age = 16
# has_id = True
# Underage

# Q-74
# choice = 5
# match choice:
#     case 1:
#         print("Add")
#     case 2:
#         print("View")
#     case 3:
#         print("Delete")
#     case _:
#         print("Invalid Choice")

# 'case _' is for all the other value which is remaining

# Q-75
# marks = 82
# attendance = 80
# if attendance >= 75:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")

# Line-60 statement is checked first because this condition decide that the code will go to inner if or go to else statemnet in line-69.