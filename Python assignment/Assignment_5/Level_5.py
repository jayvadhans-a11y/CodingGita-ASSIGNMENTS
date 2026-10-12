# Q-37
# word=input("Enter the word: ")
# for i in range(len(word)):
#     print(i,word[i])

# Q-38
# word=input("Enter the word: ")
# count=0
# for ch in word:
#     count += 1
# print("Length:", count)

# Q-39
# word=input("Enter the word: ").lower()
# v=0
# c=0
# for ch in word:
#     match(ch):
#         case "a" | "e" | "i" | "o" | "u":
#             v+=1
#         case _:
#             c+=1
# print("Vowel:", v)
# print("Consonent:", c)

# Q-40
# word=input("Enter the word: ")
# target=input("Enter the target character: ")
# count=0
# for ch in word:
#     if target==ch:
#         count=count+1
# print("Character Frequency:", count)

# Q-41
# word=input("Enter the word: ")
# target=input("Enter the target character: ")
# first_occurance=0
# for i in range(len(word)):
#     if word[i]==target:
#         if first_occurance==0:
#             first_occurance=i
# if first_occurance==0:
#     print("Not Found")
# else:
#     print("First occurance:", first_occurance)

# Q-42
# word=input("Enter the word: ")
# uppercase=0
# lowercase=0
# for ch in word:
#     if ch==ch.upper():
#         uppercase=uppercase+1
#     else:
#         lowercase=lowercase+1
# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)

# Q-43
# word=input("Enter the word: ")
# for ch in word:
#     print(ch,ord(ch))

# Q-44
# word=input("Enter the word: ")
# word1=""
# for ch in word:
#     match(ch):
#         case "a" | "e" | "i" | "o" | "u":
#             word1 = word1
#         case _:
#             word1 += ch
# print("Word without Vowel:", word1)