# Q-53
# import math
# num=int(input("Enter a number: "))
# num=abs(num)
# val=int(math.log10(num))+1
# max = 0
# max2 = 0
# for i in range(val):
#     digit = num%10
#     if max < digit:
#         max2 = max
#         max = digit
#     elif max2 < digit < max:
#         max2 = digit
#     num = num // 10
# print("Second Largest digit=", max2)


# Q-54
# string=input("Enter A string: ")
# current_Count=1
# best_count=0
# for i in range(1, len(string)):
#     current_character=string[i]
#     previous_character=string[i-1]
#     if current_character==previous_character:
#         current_Count+=1
#     else:
#         current_Count=1
#     if best_count<current_Count:
#         best_count=current_Count
# print("Longest consecutive run of the same character:", best_count)

# Q-55
# word=input("Enter the word: ")
# target=input("Enter the target character: ")
# count=0
# for ch in word:
#     if target==ch:
#         count=count+1
# frequency=(count/len(word))*100
# print(f"Count: {count}, Frequency: {frequency:.2f}%")

# Q-56
# import math
# num=int(input("Enter a positive Integer: "))
# val=int(math.log10(num))+1
# sum=0
# for i in range(val):
    # digit=num % 10
#     sum+=digit
#     num //= 10
#     print("Sum:",sum)

# Q-57
# import math
# num=int(input("Enter a positive Integer: "))
# val=int(math.log10(num))+1
# even_digit=0
# odd_digit=0
# for i in range(val):
#     digit=num % 10
#     if digit%2==0:
#         even_digit+=1
#     else:
#         odd_digit+=1
#     num//=10
# if even_digit > odd_digit:
#     print("More Even Digits")
# elif even_digit == odd_digit:
#     print("Equal")
# else:
#     print("More Odd Digits")

# Q-58
# import math
# num=int(input("Enter a number: "))
# val=int(math.log10(num)+1)
# alternating_digit_sum=0
# j=0
# for i in range(val,-1,-1):
#     digit=num%10
#     if j%2==0:
#         alternating_digit_sum+=digit
#     else:
#         alternating_digit_sum-=digit
#     j+=1
#     num=num//10
# print("Alternating Digit sum:", alternating_digit_sum)

# Q-59
# Line-1= 2
# Line-2= 6
# Line-3= 12
# Line-4= 20
# Line-5= 30

# Q-60
# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1
# print(count)
# final value = 5
# Explaination = because in this question we only increment count when the value of i is even and set the value of i from 1 to 11 means there are 10 values of i from which 5 is even and 5 is odd that's why the answer is 5.

# Q-61
# sum = 0                 # Here we create a variable sum and assign it a value 0.
# for i in range(1, 6):   # here we create a for loop and give it a range 1->6 means the loop will repeate 5 times and stop at i=6 but do not include i=6.
#     sum += i            # here we add the new value of i in sum every time the loop repeate.
# print(sum)              # here we print the final value of sum when the loop end.