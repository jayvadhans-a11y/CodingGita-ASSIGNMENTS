# Q-36
# username=input("Enter username: ")
# password=input("Enter your Password: ")
# if username=="admin":
#     if password=="admin123":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid Username")

# Q-37
# age=int(input("Enter Your Age: "))
# test_status=input("Enter test status: ")
# if age>=18:
#     if test_status=="pass":
#         print("License Approved")
#     else:
#         print("Test Not Passed")
# else:
#     print("Age Not Eligible")

# Q-38
# balance=int(input("Enter Balance: "))
# withdrawal=int(input("Enter withdrawal amount: "))
# if balance>withdrawal:
#     if withdrawal%100==0:
#         print("Withdrawal Successful")
#     else:
#         print("Enter Amount in Multiples of 100")
# else:
#     print("Insufficient Balance")

# Q-39
# attendance=int(input("Enter attendance: "))
# marks=int(input("Enter marks: "))
# if attendance>=75:
#     if marks>=0:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible Due to Attendance")

# # Method-2
# attendance=int(input("Enter attendance: "))
# if attendance>=75:
#     marks=int(input("Enter marks: "))
#     if marks>=0:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible Due to Attendance")

# Q-40
# account=input("Enter Account Type: ")
# balance=int(input("Enter Balance: "))
# if account=="savings":
#     if balance>=1000:
#         print("Minimum Balance Maintained")
#     else:
#         print("Minimum Balance Not Maintained")
# else:
#     print("Unsupported Account")

# Q-41
# order=int(input("Enter Order Amount: "))
# payment=input("Enter Payment Method: ")
# if order>=500:
#     if payment in ["card", "upi"]:
#         print(f"{payment.upper()} Payment Accepted")
#     else:
#         print("Unsupported Payment Method")
# else:
#     print("Minimum Order Amount Not Reached")

# Q-42
# year=int(input("Enter Year of Study: "))
# attendance=int(input("Enter attendance: "))
# if 4>=year>1:
#     if attendance>75:
#         print("Room Eligible")
#     else:
#         print("Attendance Too Low")
# else:
#     print("Not Eligible by Year")

# Q-43
# plan=input("Enter Current Plan: ")
# usage=int(input("Enter Monthly Usage: "))
# if plan=="basic":
#     if usage>100:
#         print("Recommend Upgrade")
#     else:
#         print("Basic Plan Is Sufficient")
# else:
#     print("Already on Higher Plan")