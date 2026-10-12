# Q-45
# word=input("Enter the word: ")
# for i in range(len(word)//2+1):
#     index=i
# print("Middle Character:", word[index])

# Q-46
# word=input("Enter a word: ")
# first_Half=""
# second_Half=""
# for i in range(len(word)):
#     if i < len(word)//2:
#         first_Half+=word[i]
#     else:
#         second_Half+=word[i]
# print("First Half:", first_Half)
# print("Seocnd Half:", second_Half)

# Q-47
# word=input("Enter a word: ")
# first_Half=""
# middle=""
# second_Half=""
# for i in range(len(word)):
#     if len(word)%2!=0:
#         if i < len(word)//2:
#             first_Half+=word[i]
#         elif i == len(word)//2:
#             middle+=word[i]
#         else:
#             second_Half+=word[i]
#     else:
#         if i < len(word)//2:
#             first_Half+=word[i]
#         else:
#             second_Half+=word[i]
# if len(word)%2==0:
#     print("First Half:", first_Half)
#     print("Seocnd Half:", second_Half)
# else:
#     print("First Half:", first_Half)
#     print("Middle Character:", middle)
#     print("Seocnd Half:", second_Half)

# Q-48
# word=input("Enter a word: ")
# first_Half=""
# second_Half=""
# for i in range(len(word)):
#     if i < len(word)//2:
#         first_Half+=word[i]
#     else:
#         second_Half+=word[i]
# if first_Half==second_Half:
#     print("Equal Halves")
# else:
#     print("Different Halves")

# Q-49
# First method
# word=input("Enter a string: ")
# word1=""
# for ch in word:
#     word1=ch+word1
# if word1==word:
#     print("Symmetric")
# else:
#     print("Not Symmetric")

# Second Method
# word=input("Enter a string: ")
# flag="true"
# for i in range(len(word)):
#     if word[i]!=word[len(word)-1-i]:
#         flag="false"
# if flag=="true":
#     print("Symmetric")
# else:
#     print("Not Symmetric")

# Q-50
# word=input("Enter a word: ")
# even_chracter=""
# for i in range(len(word)):
#     if i%2==0:
#         even_chracter+=word[i]
# print("Character at even index:", even_chracter)

# Q-51
# word=input("Enter a word: ")
# even_index=0
# odd_index=0
# for i in range(len(word)):
#     if i%2==0:
#         even_index+=1
#     else:
#         odd_index+=1
# print(f"Even index: {even_index}, Odd index: {odd_index}")

# Q-52
# word=input("Enter a word: ")
# new_word=""
# for i in range(len(word)):
#     if i%2==0:
#         new_word+=word[i+1]
#     else:
#         new_word+=word[i-1]
# print(new_word)