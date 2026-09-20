# Q-21
# number=583
# ones_digit=number%100%10
# print("ones digit:", ones_digit)

# Q-22
# number=583
# tens_digit=(number%100)//10
# print("tens digit:", tens_digit)

# Q-23
# number=583
# hundreds_digit=number//100
# print("hundreds digit:", hundreds_digit)

# Q-24
# number=746
# hundreds_digit=number//100
# tens_digit=(number%100)//10
# ones_digit=number%100%10
# print("ones digit:", ones_digit)
# print("tens digit:", tens_digit)
# print("hundreds digit:", hundreds_digit)

# Q-25
# number=5829
# ones_digit=(number%1000)%100%10
# tens_digit=(number%1000)%100//10
# hundreds_digit=(number%1000)//100
# thousands_digit=number//1000
# print("ones digit:", ones_digit)
# print("tens digit:", tens_digit)
# print("hundreds digit:", hundreds_digit)
# print("thousands digit:", thousands_digit)

# Q-26
# number=583
# hundreds_digit=number//100
# tens_digit=(number%100)//10
# ones_digit=number%100%10
# sum_of_digits=hundreds_digit+tens_digit+ones_digit
# print("sum of digits:", sum_of_digits)

# Q-27
# number=4726
# ones_digit=(number%1000)%100%10
# tens_digit=(number%1000)%100//10
# hundreds_digit=(number%1000)//100
# thousands_digit=number//1000
# sum_of_digits=thousands_digit+hundreds_digit+tens_digit+ones_digit
# print("sum of digits:", sum_of_digits)

# Q-28
# number=234
# ones_digit=(number%100)%10
# tens_digit=(number%100)//10
# hundreds_digit=number//100
# product_of_three_digits=ones_digit*tens_digit*hundreds_digit
# print("ones digit:", ones_digit)
# print("tens digit:", tens_digit)
# print("hundreds digit:", hundreds_digit)
# print("Product of three digits:", product_of_three_digits)

# Q-29
# number=583
# ones_digit=str((number%100)%10)
# tens_digit=str((number%100)//10)
# hundreds_digit=str(number//100)
# reverse_digit=ones_digit+tens_digit+hundreds_digit
# print("Original number:", number)
# print("reversed number:", reverse_digit)

# Q-30
# number=4726
# ones_digit=str(((number%1000)%100)%10)
# tens_digit=str(((number%1000)%100)//10)
# hundreds_digit=str((number%1000)//100)
# thousands_digit=str((number//1000))
# reverse_digit=ones_digit+tens_digit+hundreds_digit+thousands_digit
# print("Original number:", number)
# print("reversed number:", reverse_digit)

# Q-31
# number=5834
# ones_place=((number%1000)%100)%10
# tens_place=((number-ones_place)%1000)%100
# hundreds_place=(number-tens_place-ones_place)%1000
# thousands_place=(number-hundreds_place-tens_place-ones_place)
# print("ones Place:", ones_place)
# print("tens Place:", tens_place)
# print("hundreds Place:", hundreds_place)
# print("thousands Place:", thousands_place)

# Q-32
# number=583
# ones_digit=(number%100)%10
# hundreds_digit=number//100
# difference=hundreds_digit-ones_digit
# print("Difference:", difference)

# Q-33
# number=583
# ones=number%10
# print("Ones Digit:", ones)

# Q-34
# number=9365
# ones_digit=(number%1000)%100%10
# tens_digit=(number%1000)%100//10
# hundreds_digit=(number%1000)//100
# thousands_digit=number//1000
# print("ones digit:", ones_digit)
# print("tens digit:", tens_digit)
# print("hundreds digit:", hundreds_digit)
# print("thousands digit:", thousands_digit)

# Q-35
# hundreds=5
# tens=8
# ones=3
# number=str(hundreds)+str(tens)+str(ones)
# print("Number:", number)