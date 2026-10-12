# Q-23
# import math
# num=int(input("Enter a positive number: "))
# val=int(math.log10(num))+1
# count=0
# for i in range(val):
#     count += 1
# print("Count =", count)

# Q-24
# num = int(input("Enter a number: "))
# sum = 0
# for ch in str(num):
#     sum += int(ch)
# print("Sum of Digits:", sum)

# Q-25
# num = int(input("Enter a number: "))
# product = 1
# for ch in str(num):
#     product *= int(ch)
# print("Product of Digits:", product)

# Q-26
# num = int(input("Enter a number: "))
# count = 0
# for ch in str(num):
#     if int(ch)%2==0:
#         count += 1
# print("Even Digit:", count)

# Q-27
# num = int(input("Enter a number: "))
# sum = 0
# for ch in str(num):
#     if int(ch)%2==0:
#         sum += int(ch)
# print("Even Digit sum:", sum)

# Q-28
# import math
# num=int(input("Enter a number: "))
# num=abs(num)
# val=int(math.log10(num))+1
# max = 0
# for i in range(val):
#     digit = num%10
#     if max < digit:
#         max = digit
#     num = num // 10
# print("Largest digit=", max)

# Q-29
# import math
# num=int(input("Enter a number: "))
# num=abs(num)
# val=int(math.log10(num))+1
# min = 9
# for i in range(val):
#     digit = num%10
#     if min > digit:
#         min = digit
#     num = num // 10
# print("Smallest digit=", min)

# Q-30
# import math
# num=int(input("Enter a number: "))
# val=int(math.log10(num))+1
# rev=0
# for i in range(val):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print("Reverse number:", rev)

# Q-31
# num=input("Enter a number: ")
# num1=""
# for ch in num:
#     num1=ch+num1
# if num1==num:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Q-32
# num=int(input("Enter a number: "))
# digit=int(input("Enter the target number: "))
# count=0
# for i in str(num):
#     if i==str(digit):
#         count += 1
# print("Count:", count)

# Q-33
# import math
# num=int(input("Enter a number: "))
# val=int(math.log10(num))+1
# for i in range(val):
#     digit=num%10
#     num=num//10
# print("First digit:", digit)

# Q-34
# import math
# num=int(input("Enter a number: "))
# num=abs(num)
# val=int(math.log10(num))+1
# max = 0
# min = 9
# for i in range(val):
#     digit = num%10
#     if max < digit:
#         max = digit
#     if min > digit:
#         min = digit
#     num = num // 10
# print("Difference btw largest and smallest digit:", max-min)

# Q-35
# import math
# num=int(input("Enter a number: "))
# val=int(math.log10(num))+1
# for i in range(1, val+1):
#     digit=num%10
#     print(digit, i)
#     num=num//10

# Q-36
# num=int(input("Enter a three digit number: "))
# num1=0
# for i in str(num):
#     num1=num1+(int(i)**(len(str(num))))
# if num==num1:
#     print("Armstrong")
# else:
#     print("Not a Armstrong")