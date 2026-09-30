# Q-44
# Method-1
# a=int(input("Enter number A: "))
# b=int(input("Enter number B: "))
# c=int(input("Enter number C: "))
# if a>b and a>c:
#     print("A is greater")
# elif b>c and b>a:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# elif a>c and a==b:
#     print("A and B are Equal and Greatest")
# elif a>b and a==c:
#     print("A and C are Equal and Greatest")
# elif b>a and b==c:
#     print("B and C are Equal and Greatest")
# else:
#     print("All are Equal")

# Method-2
# a=int(input("Enter number A: "))
# b=int(input("Enter number B: "))
# c=int(input("Enter number C: "))
# if a>b:
#     if a>c:
#         print("A is Greatest")
#     elif a<c:
#         print("C is Greatest")
#     else:
#         print("A and C are Equal and Greatest")
# elif b>c:
#     if b>a:
#         print("B is Greatest")
#     else:
#         print("A and B are Equal and Greatest")
# else:
#     if c>a:
#         print("C is Greatest")
#     elif c==b:
#         print("B and C are Equal and Greatest")
#     else:
#         print("All are Equal")


# Q-45
# attendance=int(input("Enter attendance: "))
# marks=int(input("Enter Marks: "))
# if attendance>=75:
#     if marks>=90:
#         print("Grade-A")
#     elif marks>=75:
#         print("Grade-B")
#     elif marks>=60:
#         print("Grade-C")
#     elif marks>=40:
#         print("Grade-D")
#     else:
#         print("Grade-F")
# else:
#     print("Not Eligible")

# Q-46
# salary=int(input("Enter Salary: "))
# performance=int(input("Enter Performance Rating: "))
# if salary>=30000:
#     if performance==5:
#         print("Bonus: 20%")
#     elif performance==4:
#         print("Bonus: 15%")
#     elif performance==3:
#         print("Bonus: 10%")
#     else:
#         print("Bonus: 5%")
# else:
#     print("Not Eligible for Bonus")

# Q-47
# age=int(input("Enter age: "))
# distance=int(input("Enter distance: "))
# if 5>age:
#     print("Free")
# elif 59>=age>=5:
#     print("Regular")
#     if 10>=distance:
#         print("Short Distance")
#     else:
#         print("Long Distance")
# else:
#     print("Senior")

# Q-48
# stock=int(input("Enter product stock: "))
# status=input("Enter payment status: ")
# if stock>0:
#     if status=="paid":
#         print("Order Confirmed")
#     elif status=="pending":
#         print("Payment Pending")
#     else:
#         print("Invalid Payment Status")
# else:
#     print("Out of Stock")

# Q-49
# age=int(input("Enter age: "))
# ticket=input("Enter ticket type: ")
# if 5>age:
#     print("Free Travel")
# elif 59>=age>=5:
#     print("Regular Passenger")
#     if ticket=="AC":
#         print("AC Ticket")
#     elif ticket=="Sleeper":
#         print("Sleeper Ticket")
#     else:
#         print("Invalid Ticket Type")
# else:
#     print("Senior Passanger")