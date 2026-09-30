# Q-58
# id=input("Enter id: ").split("-")
# degree, batch, branch, roll_number=id
# if branch=="CSE":
#     print("CSE Student")
# else:
#     print("Non-CSE Student")

# Q-59
# email=input("Enter email id: ").split("@")
# name, domain=email
# if domain=="gmail.com":
#     print("Gmail User")
# else:
#     print("Other Email Provider")

# Q-60
# name=input("Enter full name containing 3 word: ").split()
# first_name, middle_name, last_name=name
# username=first_name+"."+last_name
# if "." in username:
#     print("Valid Username Format")
# else:
#     print("Invalid Username Format")

# Q-61
# num=int(input("Enter a positive integer: "))
# if 10>num:
#     print("One Digit")
# elif 100>num:
#     print("Two Digits")
# elif 1000>num:
#     print("Three Digits")
# else:
#     print("Four or More Digits")

# Q-62
# price=int(input("Enter Product price: "))
# quantity=int(input("Enter Product quality: "))
# subtotal = price * quantity
# if 2000>subtotal:
#     discount=0
# elif 5000>subtotal:
#     discount=10
# else:
#     discount=20
# final=subtotal-(subtotal*discount/100)
# print(f"Subtotal: {subtotal}, Discount: {discount}%, Final: {final:.2f}")

# Q-63
# unit=int(input("Enter total unit: "))
# if 100>=unit:
#     rate=5
# elif 300>=unit:
#     rate=7
# else:
#     rate=10
# bill=unit*rate
# print(f"Rate: ₹{rate}, Bill: ₹{bill}")

# Q-64
# print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
# choice=int(input("Enter your choice: "))
# balance=10000
# match choice:
#     case 1:
#         print("Balance:", balance)
#     case 2:
#         amount=int(input("Enter Amount: "))
#         print(f"Withdrawal Successful, Balance: {balance+amount}")
#     case 3:
#         amount=int(input("Enter Amount: "))
#         if amount>balance:
#             print("Insufficient Balance")
#         else:
#             print(f"Withdrawal Successful, Balance: {balance-amount}")
#     case 4:
#         print("Exit")
#     case _:
#         print("Invalid Choice")

# Q-65
# choice=int(input("Enter your choice: "))
# quantity=int(input("Enter quantity: "))
# match choice:
#     case 1:
#         item="Pizza"
#         price=250
#     case 2:
#         item="Burger"
#         price=150
#     case 3:
#         item="Pasta"
#         price=200
#     case 4:
#         item="Sandwich"
#         price=120
#     case _:
#         print("Invalid Choice")
# total = price * quantity
# if total >= 500:
#     discount = total * 10 / 100
# else:
#     discount = 0
# final=total-discount
# print(f"Total: {total}, Discount: {discount:.2f}, Final: {final:.2f}")                                                                               

# Q-66
# sub1=int(input("Enter subject1 marks: "))
# sub2=int(input("Enter subject2 marks: "))
# sub3=int(input("Enter subject3 marks: "))
# attendance=int(input("Enter attendance: "))
# average=(sub1+sub2+sub3)/3
# if attendance>=75:
#     if average>=90:
#         print("Outstanding")
#     elif average>=75:
#         print("Very Good")
#     elif average>=60:
#         print("Good")
#     elif average>=40:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")


# Q-67
# distance = int(input("Enter distance: "))
# ride_type = input("Enter Ride type: ")
# match ride_type:
#     case "normal":
#         rate = 15
#     case "premium":
#         rate = 25
#     case _:
#         print("Invalid Ride Type")
# if distance > 20:
#     surcharge = 10
# else:
#     surcharge = 0
# fare = distance * rate
# final_fare = fare + (fare*10/100)
# print(f"Fare: {final_fare:.2f}")

# Q-68
# score = int(input("Enter Entrance score: "))
# percentage = int(input("Enter 12th Percentage: "))
# category = input("Enter category: ")
# match category:
#     case "general":
#         if score >= 80 and percentage >=75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "obc":
#         if score >= 70 and percentage >= 70:    
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "sc":
#         if score >= 60 and percentage >= 60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case _:
#         print("Invalid Category")