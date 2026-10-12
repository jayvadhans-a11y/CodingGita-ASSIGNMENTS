# Q-68
# import math
# num=int(input("Enter the number: "))
# val=int(math.log10(num))+1
# sum=0
# largest=0
# smallest=10
# even_digit=0
# odd_digit=0
# for i in range(val):
#     digit=num%10
#     sum+=digit
#     if largest<digit:
#         largest=digit
#     if smallest>digit:
#         smallest=digit
#     if digit%2==0:
#         even_digit+=1
#     else:
#         odd_digit+=1
#     num=num//10
# print("Digits:", val)
# print("Sum:", sum)
# print("Largest:", largest)
# print("Smallest:", smallest)
# print("Even Digits:", even_digit)
# print("Odd Digits:", odd_digit)

# Q-69
# string=input("Enter a string: ")
# vcount=0
# ccount=0
# upper_count=0
# lower_count=0
# even_index=0
# total_chr=len(string)
# for i in range(total_chr):
#     match(string[i].lower()):
#         case 'a' | 'e' | 'i' | 'o' | 'u':
#             vcount+=1
#         case " ":
#             space=1
#         case _:
#             ccount+=1
#     if string[i]==" ":
#         space=1
#     elif string[i]==string[i].upper():
#         upper_count+=1
#     else:
#         lower_count+=1
#     if i%2==0:
#         even_index+=1
# print("Total character:",total_chr)
# print("Vowels:", vcount)
# print("Consonents:", ccount)
# print("Uppercase:", upper_count)
# print("Lowercase:", lower_count)
# print("Even Index Character:", even_index)