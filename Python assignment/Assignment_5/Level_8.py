# Q-62
# days=int(input("Enter the number of days: "))
# expenses=input("Enter the expenses: ").split(" ")
# total_expenses=0
# highest_expenses=0
# lowest_expenses=100000
# for ch in expenses:
#     digit=int(ch)
#     total_expenses+=digit
#     if highest_expenses < digit:
#         highest_expenses=digit
#     if lowest_expenses > digit:
#         lowest_expenses=digit
# print(f"Total expense: {total_expenses}\nHighest Expense: {highest_expenses}\nLowest Expense: {lowest_expenses}")

# Q-63
# subjects=int(input("Enter the number of Subjects: "))
# marks=input("Enter the marks: ").split(" ")
# total_marks=0
# highest_marks=0
# lowest_marks=100
# for ch in marks:
#     digit=int(ch)
#     total_marks+=digit
#     if highest_marks < digit:
#         highest_marks=digit
#     if lowest_marks > digit:
#         lowest_marks=digit
# average_marks=total_marks//subjects
# print("Total marks:", total_marks)
# print("Average marks:", average_marks)
# print("Highest marks:", highest_marks)
# print("Lowest marks:", lowest_marks)

# Q-64
# days=int(input("Enter the number of days: "))
# status=input("Enter the attendance: ").split(" ")
# present_count=0
# absent_count=0
# for ch in status:
#     if ch=="p":
#         present_count+=1
#     else:
#         absent_count+=1
# average_attendance=(present_count*100/days)
# print("Present count:", present_count)
# print("Absent count:", absent_count)
# print(f"Average attendance: {average_attendance:.2f}%")

# Q-65
# days=int(input("Enter the number of days: "))
# units=input("Enter the elctricity Unis of each day: ").split(" ")
# total_units=0
# above_count=0
# for ch in units:
#     digit=int(ch)
#     total_units+=digit
#     if digit>10:
#         above_count+=1
# print("Total units:", total_units)
# print("Days above 10:", above_count)

# Q-66
# n=int(input("Enter the number of products: "))
# prices=input("Prices: ").split(" ")
# total_bill=0
# above_count=0
# for ch in prices:
#     digit=int(ch)
#     total_bill+=digit
#     if digit>1000:
#         above_count+=1
# print("Total bill:", total_bill)
# print("Product Above 1000:", above_count)


# Q-67
# n=int(input("Enter the number of attempt: "))
# attempt=input("Enter the result of each attempt: ").split(" ")
# success_count=0
# fail_count=0
# for ch in attempt:
#     if ch=="success":
#         success_count+=1
#     else:
#         fail_count+=1
# success_rate=success_count*100/n
# print("Successful:", success_count)
# print("Failed:", fail_count)
# print(f"Success_rate: {success_rate}%")