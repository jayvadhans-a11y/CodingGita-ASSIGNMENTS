# Q-60
# name=input("Student name: ")
# a,b,c=input("Enter three subject marks with gap: ").split()
# total=int(a)+int(b)+int(c)
# average=(int(a)+int(b)+int(c)/3)
# print(f"Name: {name}\nTotal: {total}\nAverage: {average:.2f}")

# Q-61
# id=input("Enter id: ").split("-")
# print(f"Degree: {id[0]}\nBatch: {id[1]}\nBranch: {id[2]}\nRoll Number: {int(id[3])}")

# Q-62
# name=input("Enter a three word full name: ")
# words = name.split()
# username = words[0].lower() + "." + words[2].lower()
# print(username)

# Q-63
# sentence=input("Enter the sentence: ").split()
# print(f"First word: {sentence[0]}\nLast word: {sentence[-1]}\nNumber of words: {len(sentence)}")

# Q-64
# email = input("Enter email: ")
# parts = email.split("@")
# print(f"@ Present: {"@" in email}\nUsername: {parts[0]}\nDomain: {parts[1]}")

# Q-65
# character=input("Enter a character: ")
# print(f"Character: {character}\nCode: {ord(character)}\nPrevious: {chr(ord(character)-1)}\nNext: {chr(ord(character)+1)}")

# Q-66
# product_name=input("Enter product name: ")
# price=int(input("Enter product price: "))
# quantity=int(input("Enter product quantity: "))
# discount_percentage=int(input("Enter product discount pencentage: "))
# subtotal = price * quantity
# discount = subtotal * discount_percentage / 100
# final_Total = subtotal - discount
# print(f"Product: {product_name}\n Price: {price:.2f}\n Quantity: {quantity}\n Subtotal: {subtotal:.2f}\n Discount: {discount:.2f}\n Final total: {final_Total:.2f}")

# Q-67
# date=input("Enter date: ").split("-")
# print("Day:", date[0])
# print("Month:", date[1])
# print("Year:", date[2])

# Q-68
# sentence=input("Enter the sentence: ").split()
# print("First Word:", sentence[0])
# print("Second Word:", sentence[1])
# print("First Word Reversed:", (sentence[0])[-1::-1])
# print("Second Word Reversed:", (sentence[1])[-1::-1])

# Q-69
# id=input("Enter id: ").split("-")
# print(f"Degree: {id[0]}\nBatch: {id[1]}\nBranch: {id[2]}\nRoll Number: {int(id[3])}\nCode: {id[0]}\\{id[2]}\\{id[3]}")

# Q-70
# name0=input("Enter full name: ")
# name1=name0.split()
# print("Original:", name0)
# print("First Name:", name1[0])
# print("Last Name:", name1[-1])
# print("First Name (Upper Part):", (name1[0])[0:3].upper())
# print("Last Name (Lower Part):", (name1[-1])[1:4].lower())
# print("Full Name Reversed:", name0[-1::-1])