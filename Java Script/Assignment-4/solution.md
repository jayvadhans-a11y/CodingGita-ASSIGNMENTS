# Assignment : Conditional Statements

---

### A] `if` Statement 

1. Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.

**Answer**
```js
let num=45
if(num%5==0){
    console.log("Divisible by 5")
}
```

2. Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.

**Answer**
```js
let age=60
if(age>=60){
    console.log("Senior Citizen")
}
```

3. Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.

**Answer**
```js
let num=101
if(num>100){
    console.log("Big Number")
}
```

4. Check if the temperature is less than 10. If true, print “Very Cold”.

**Answer**
```js
let temperature=6
if(temperature<10){
    console.log("Very Cold")
}
```

5. Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.

**Answer**
```js
let marks=100
if(marks==100){
    console.log("Perfect Score")
}
```

6. Check if a number is negative. If it is, print “Negative Number”.

**Answer**
```js
let num=-5
if(num<0){
    console.log("Negative number")
}
```

7. Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.

**Answer**
```js
let word=""
if(word==0){
    console.log("No input provided")
}
```

8. Check if a given year is divisible by 100. If yes, print “Century Year”.

**Answer**
```js
let year=2000
if(year%100==0){
    console.log("Century Year")
}
```

9. Write a program to check if a number is both positive and even using a single `if` condition. If true, print “Positive Even Number”.

**Answer**
```js
let num=8
if(num>0 && num%2==0){
    console.log("Positive even number")
}
```

10. Check if the value of a variable `marks` is greater than or equal to 35 **and** less than or equal to 100. If true, print “Valid Marks”.

**Answer**
```js
let marks=65
if(marks>35 && marks<=100){
    console.log("Valid marks")
}
```

---

### B] `if...else` Statement 

1. Write a program to check whether a number is even or odd.

**Answer**
```js
let num=7
if(num%2==0){
    console.log("Even number")
}
else{
    console.log("Odd number")
}
```

2. Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.

**Answer**
```js
let age=18
if(age>=18){
    console.log("Eligible")
}
else{
    console.log("Not Eligible")
}
```

3. Write a program that checks whether a number is positive or negative.

**Answer**
```js
let num=15
if(num>=0){
    console.log("positive")
}
else{
    console.log("negative")
}
```

4. Check if a student has passed or failed based on marks (pass mark = 35).

**Answer**
```js
let marks=35
if(marks>=35){
    console.log("Passed")
}
else{
    console.log("Failed")
}
```

5. Write a program to check whether a given character is an uppercase letter or not.  
   (Hint: Use character comparison)

**Answer**
```js
let character="A"
if(character==character.toUpperCase()){
    console.log("Uppercase Letter")
}
else{
    console.log("Lowercase Letter")
}
```

6. Check if a number is divisible by 3 or not. Print appropriate messages.

**Answer**
```js
let num=6
if(num%3==0){
    console.log("Divisible by 3")
}
else{
    console.log("Not divisible by 3")
}
```

7. Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.

**Answer**
```js
let password = "admin123"
if(password == "admin123"){
    console.log("Login Successful")
}
else{
    console.log("Incorrect password")
}
```

8. Check whether a given year is a leap year or not using the basic rule (divisible by 4).

**Answer**
```js
let year = 2024
if(year%4==0){
    console.log("Leap year")
}
else{
    console.log("normal year")
}
```

9. Write a program to find the greater of two numbers using `if...else`.

**Answer**
```js
let num1 = 20
let num2 = 59
if(num1>num2){
    console.log(`${num1} is greater`)
}
else{
    console.log(`${num2} is greater`)
}
```

10. Check if a number is positive, negative, or zero using only `if...else` (you may use nested or multiple conditions carefully).

**Answer**
```js
let num = 46
if(num>=0){
    if(num>0){
        console.log("Positive")
    }
    else{
        console.log("Zero")
    }
}
else{
    console.log("Negative")
}
```


### C] `if...else if...else` Statement 


1. Write a program that takes a month number (1–12) and prints the corresponding season:  
   Winter (12, 1, 2), Summer (3, 4, 5), Monsoon (6, 7, 8), Autumn (9, 10, 11).

   **Answer**
```js
let monthNumber = 8
if(monthNumber == 12 || monthNumber == 1 || monthNumber == 2 ){
    console.log("Winter")
}
else if(monthNumber == 3 || monthNumber == 4 || monthNumber == 5 ){
    console.log("Summer")
}
else if(monthNumber == 6 || monthNumber == 7 || monthNumber == 8 ){
    console.log("Monsoon")
}
else if(monthNumber == 9 || monthNumber == 10 || monthNumber == 11 ){
    console.log("Autumn")
}
else{
    console.log("Wrong Month Number")
}
```

2. Create a simple tax calculator based on income:  
   Income < 3,00,000 → No tax  
   3,00,000 – 7,00,000 → 5% tax  
   7,00,000 – 10,00,000 → 10% tax  
   Above 10,00,000 → 15% tax  
   Print the tax amount.

   **Answer**
```js
let income = 700000
if(income < 300000){
    console.log(0)
}
else if(income < 700000){
    console.log(income*0.05)
}
else if(income < 1000000){
    console.log(income*0.10)
}
else{
    console.log(income*0.15)
}
```

3. Write a program that checks a student’s score and prints:  
   “Outstanding” (90 and above), “Good” (70–89), “Average” (40–69), “Needs Improvement” (below 40).

   **Answer**
```js
let marks = 80
if(marks >= 90){
    console.log("Outstanding")
}
else if(marks >= 70){
    console.log("Good")
}
else if(marks >= 40){
    console.log("Average")
}
else{
    console.log("Needs Improvement")
}
```

4. Check the speed of a vehicle and print:  
   “Slow” (below 40), “Normal” (40–80), “Fast” (above 80).

   **Answer**
```js
let speedOfVehicle = 40
if(speedOfVehicle > 80){
    console.log("Fast")
}
else if(speedOfVehicle >= 40){
    console.log("Normal")
}
else{
    console.log("Slow")
}
```

5. Write a program that checks a person’s height (in cm) and prints:  
   “Short” (< 150), “Average” (150–170), “Tall” (> 170).

   **Answer**
```js
let height = 178
if(height > 170){
    console.log("Tall")
}
else if(height >= 150){
    console.log("Average")
}
else{
    console.log("Short")
}
```

6. Check the day number (1–7) and print whether it is a Weekday or Weekend  
   (1 to 5 = Weekday, 6 and 7 = Weekend).

   **Answer**
```js
let dayNumber = 5
if(dayNumber >= 1 && dayNumber<=5){
    console.log("Weekday")
}
else if(dayNumber >= 6 && dayNumber<=7){
    console.log("Weekend")
}
else{
    console.log("Invalid day number")
}
```

7. Write a program that calculates electricity bill based on units:  
   0–50 units → ₹2 per unit  
   51–150 units → ₹4 per unit  
   Above 150 units → ₹6 per unit  
   Print the total bill.

   **Answer**
```js
let units = 45
if(units>=0 && units<=50){
    bill = units*2
}
else if(units<=150){
    bill=units*4
}
else{
    bill=units*6
}
console.log("Total bill=", bill)
```

8. Create a program that checks a student’s attendance percentage and prints:  
   “Excellent” (≥ 90), “Good” (75–89), “Satisfactory” (50–74), “Poor” (< 50).

   **Answer**
```js
let attendance = 99
if(attendance >= 90){
    console.log("Excellent")
}
else if(attendance >= 75){
    console.log("Good")
}
else if(attendance >= 50){
    console.log("Satisfactory")
}
else{
    console.log("Poor")
}
```

9. Write a program that takes three subject marks and finds the highest mark among them using `if...else if...else`.

   **Answer**
```js
let marks1 = 93
let marks2 = 87
let marks3 = 80
if(marks1>marks2 && marks1>marks3){
    largest=marks1
}
else if(marks2>marks1 && marks2>marks3){
    largest=marks2
}
else{
    largest=marks3
}
console.log("Highest marks is", largest)
```

10. Check a number and print one of the following:  
    “Positive Even”, “Positive Odd”, “Negative Even”, “Negative Odd”, or “Zero”.

   **Answer**
```js
let num = 7
if(num>0 && num%2==0){
    console.log("Positive Even")
}
else if(num>0 && num%2!=0){
    console.log("Positive Odd")
}
else if(num<0 && num%2==0){
    console.log("Negative Even")
}
else if(num<0 && num%2!=0){
    console.log("Negative Odd")
}
else{
    console.log("Zero")
}
```

---


### D] Nested `if` Statement 


1. Check if a number is greater than 10.  
   If yes, then check whether it is divisible by 3 and print the appropriate message.

   **Answer**
```js
let num = 15
if(num>10){
    if(num%3==0){
        console.log("number is greater than 10 and divisible by 3")
    }
}
```

2. Write a program that first checks if a person is 18 or older.  
   If yes, then check if they have a voter ID. Print “Can Vote” only if both conditions are true.

   **Answer**
```js
let age = 20
let hasVoterId = true
if(age>=18){
    if(hasVoterId){
        console.log("Can Vote")
    }
}
```

3. Check if a student has scored 40 or more marks.  
   If yes, then check if the score is 80 or above and print “Passed with Distinction”.

   **Answer**
```js
let marks = 80
if(marks>=40){
    if(marks>=80){
        console.log("Passed with distinction")
    }
}
```

4. Create a simple ATM system:  
   First check if the PIN is correct.  
   If PIN is correct, then check if the account balance is sufficient for withdrawal.

   **Answer**
```js
let pin = 4242;
let balance = 7000
let amount = 800
if(pin==4242){
    if(amount<balance){
        console.log("Balance is sufficient for withdrawal")
    }
}
```

5. Write a program that checks if a year is divisible by 4.  
   If yes, then further check if it is divisible by 100.  
   If it is divisible by 100, then check if it is also divisible by 400 to confirm it is a leap year.

   **Answer**
```js
let year = 4000
if(year%4==0){
    if(year%100==0){
        if(year%400==0){
            console.log("yes, It is definitely a leap year")
        }
    }
}
```

6. Check if a user has entered a valid email (contains “@”).  
   If yes, then check if the email ends with “.com”.  
   If both are true, then check if the length of the email is greater than 10 characters and print “Valid Email”.

   **Answer**
```js
let email = "abc.cg@gmail.com";
if(email.includes('@')==true){
    console.log("yes");
    let l = email.length;
    let last_chars = email[l-4]+email[l-3]+email[l-2]+email[l-1];
    if(last_chars==".com"){
        if(l>10){
            console.log(`the email ${email} is valid Email`)
        }
    }
}
```

7. Write a program for online shopping:  
   First check if the cart total is ₹1000 or more.  
   If yes, then check if the user is a premium member.  
   If the user is premium, give 20% discount, otherwise give 10% discount.  
   Finally print the final amount after discount.

   **Answer**
```js
let cartTotal = 1001;
let isPrimeMember = true;
if(cartTotal >= 1000) {
    if(isPrimeMember == true){
        cartTotal -= (cartTotal * 0.20);
    }
    else{
        cartTotal -= (cartTotal * 0.10);
    }
};
console.log(cartTotal);
```

8. Check if a number is positive.  
   If yes, then check whether it is even.  
   If it is even, then further check if it is divisible by 4 and print “Positive Even and Divisible by 4”.

   **Answer**
```js
let num = 16
if(num>0){
    if(num%2==0){
        console.log("Positive Even and Divisible by 4")
    }
}
```

9. Create a job eligibility checker with multiple conditions:  
   First check if age is between 21 and 30.  
   If age is valid, then check if the candidate has a graduation degree.  
   If the degree is present, then check if the candidate has at least 2 years of experience.  
   Print “Eligible for Interview” only if all three conditions are true.

   **Answer**
```js
let age = 21;
let hasGraduationDegree = true
let experience = 2
if(age>=21 && age<=30){
    if(hasGraduationDegree){
        if(experience>=2){
            console.log("Eligible for Interview")
        }
    }
}
```

10. Write a nested program for exam eligibility:  
    First check if the student is present.  
    If present, then check if internal marks are ≥ 30.  
    If internal marks are valid, then check if external marks are ≥ 35.  
    Print “Eligible for Final Exam” only when all conditions are satisfied.

   **Answer**
```js
let isStudentPresent = true;
let internalMarks = 35
let externalMarks = 40
if(isStudentPresent){
    if(internalMarks>=30){
        if(externalMarks>=35){
            console.log("Eligible for final exam")
        }
    }
}
```

---


### E] `switch` Statement – 10 Questions

1. Write a program that takes a month number (1–12) and prints the number of days in that month using `switch`  
   (Hint: Consider 28/29 for February as 28 for simplicity).

   **Answer**
```js
let month = 8;
switch(month){
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        console.log("31 days")
        break
    case 2:
        console.log("28/29 days")
        break
    case 4:
    case 6:
    case 9:
    case 11:
        console.log("30 days")
        break
    default:
        console.log("Invalid month number");
}
```

2. Write a program that checks a character and prints whether it is a vowel or consonant using `switch`.

   **Answer**
```js
let character = "O";
switch(character.toLowerCase()){
    case "a":
    case "e":
    case "i":
    case "o":
    case "u":
        console.log("Vowel")
        break
    default:
        console.log("Consonent");
}
```

3. Create a program that takes a number from 1 to 4 and prints the season using multiple cases together:  
   1 or 2 → Winter  
   3 or 4 → Summer

   **Answer**
```js
let seasonNum = 1;
switch(seasonNum){
    case 1:
    case 2:
        console.log("winter");
        break;
    case 3:
    case 4:
        console.log("Summer");
        break;
    default:
        console.log("Invalid Number!");
}
```

4. Write a program using `switch (true)` to assign class based on marks:  
   ≥ 75 → Distinction  
   ≥ 60 → 1st class  
   ≥ 50 → 2nd class  
   ≥ 35 → 3rd class  
   below 35 → Failed

   **Answer**
```js
let marks = 55;
switch(true){
    case marks>=75:
        console.log("Distinction");
        break;
    case marks>=60:
        console.log("1st class");
        break;
    case marks>=50:
        console.log("2nd class");
        break;
    case marks>=35:
        console.log("3rd class");
        break;
    default:
        console.log("Failed");
}
```

5. Create a nested `switch` program:  
   First take a role (“admin” or “user”).  
   If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.  
   If role is “user”, print “Limited Access”.

   **Answer**
```js
let role = "admin";
let action = "create";
switch(role){
    case "admin":
        switch(action){
            case "create":
                console.log("Create action is selected");
            break
            case "edit":
                console.log("edit action is selected");
                break
            case "delete":
                console.log("delete action is selected");
                break
            default:
                console.log("Invalid action");
                break
        }
        break
    case "user":
        console.log("Limited Access");
        break;
    default:
        console.log("Invalid role");
}
```

6. Predict and explain the output of the following code. Then correct it so that only one message is printed:
```js
let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
  case "mango":
    console.log("Mango is yellow");
  case "banana":
    console.log("Banana is yellow");
  default:
    console.log("Unknown fruit");
}
```

   **Answer**
- Explaination= it print all output because we did not give break after each case so it will not stop after getting an answer and print all output
```js
let fruit = "mango";
switch (fruit) {
  case "apple":
    console.log("Apple is red");
    break
  case "mango":
    console.log("Mango is yellow");
    break
  case "banana":
    console.log("Banana is yellow");
    break
  default:
    console.log("Unknown fruit");
}
```

7. Write a program that takes a value which can be either a number or a string (`0`, `"0"`, `false`, `null`, `undefined`) and uses `switch` to correctly identify each one. Explain why some values may not match as expected.

   **Answer**
```js
let value=0
switch(true){
    case value===0:
        console.log("number")
        break;
    case value==="0":
        console.log("string")
        break;
    case value===false:
        console.log("Boolean")
        break;
    case value===null:
        console.log("null value")
        break;
    case value===undefined:
        console.log("undefined")
        break;
    default:
        console.log("invalid")
}
```

8. Create a tricky calculator using `switch` that supports these operations:  
   `+`, `-`, `*`, `/`, `%`, and also `**` (exponentiation).  
   Handle division by zero properly inside the corresponding case.

   **Answer**
```js
let num1=10
let num2=0
let operation="/"
switch(true){
    case operation==="+":
        console.log(num1+num2)
        break;
    case operation==="-":
        console.log(num1-num2)
        break;
    case operation==="*":
        console.log(num1*num2)
        break;
    case operation==="/":
        if num2==0:
            console.log("Division by 0 is not allowed")
            break
        else:
            console.log(num1/num2)
            break
        break;
    case operation==="%":
        console.log(num1%num2)
        break;   
    case operation==="**":
        console.log(num1**num2)
        break;  
    default:
        console.log("Invalid operation")   
}
```

9. Write a program using `switch` that takes a date (day number of the month) and prints:  
   “Beginning of the month” (1–10)  
   “Middle of the month” (11–20)  
   “End of the month” (21–31)  
   Use `switch (true)` technique for range checking.

   **Answer**
```js
let date = 15
switch(date){
    case date>=1 && date<=10:
        console.log("Beginning of the month")
        break
    case date<=20 && date>=11:
        console.log("Middle of the month")
        break
    case date>=21 && date<=31:
        console.log("End of the month")
        break
    default:
        console.log("Invalid date")
}
```

10. Create a multi-level nested `switch` program for an online food ordering system:  
    First select Category: `"veg"` or `"nonveg"`.  
    Then select Item based on category.  
    Finally select Size: `"half"` or `"full"` and print the final order summary with price.

   **Answer**
```js
let category="veg"
let item="paneer tikka"
let size="full"

switch(category){
    case "veg":
        switch(item){
            case "biryani":
                switch(size){
                    case "full":
                        console.log("Price of full plate biryani is ₹240")
                        break
                    case "half":
                        console.log("Price of half plate biryani is ₹120")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            case "paneer tikka":
                switch(size){
                    case "full":
                        console.log("Price of full plate paneer tikka is ₹280")
                        break
                    case "half":
                        console.log("Price of half plate paneer tikka is ₹140")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            default:
                console.log("Invalid item")
        }
        break
    case "nonveg":
        switch(item){
            case "biryani":
                switch(size){
                    case "full":
                        console.log("Price of full plate biryani is ₹280")
                        break
                    case "half":
                        console.log("Price of half plate biryani is ₹140")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            case "chicken":
                switch(size){
                    case "full":
                        console.log("Price of full plate chicken is ₹320")
                        break
                    case "half":
                        console.log("Price of half plate chicken is ₹160")
                        break
                    default:
                        console.log("Invalid size")
                }
                break
            default:
                console.log("Invalid item")
        }
        break
    default:
        console.log("Invalid category")
}
```

---

### F] Ternary Operator Questions  


1. Write a ternary operator to check whether a given number is divisible by 7. If yes, return `"Divisible by 7"`, otherwise `"Not Divisible by 7"`.

   **Answer**
```js
let num=35;
let result=num%7==0? "divisible by 7": "not divisible by 7"
console.log(result)
```

2. Using ternary operator, check if the temperature is greater than or equal to 30. Return `"Hot Day"` or `"Pleasant Day"`.

   **Answer**
```js
let temperature=26;
let result=temperature>=30? "Hot Day": "Pleasant Day"
console.log(result)
```

3. Write a ternary expression that checks if a string is empty. Return `"Empty String"` if it is empty, otherwise `"String has content"`.


   **Answer**
```js
let isStringEmpty=true;
let result=isStringEmpty? "Empty String": "String has content"
console.log(result)
```

4. Using nested ternary, check a person’s age and return:  
   - `"Child"` (age < 13)  
   - `"Teenager"` (13–19)  
   - `"Adult"` (20 and above)

   **Answer**
```js
let age=16;
let result=age<13? "Child": age<=19? "Teenager" : "Adult"
console.log(result)
```

5. Write a nested ternary to find the greater of three numbers (`a`, `b`, `c`) without using `Math.max`.

   **Answer**
```js
let a=9;
let b=2;
let c=8;
let result=a>b && a>c? `${a} is greater` : b>a && b>c? `${b} is greater` : `${c} is greater`
console.log(result)
```

6. Create a nested ternary that classifies a student’s marks as:  
   - `"Distinction"` (≥ 75)  
   - `"First Class"` (60–74)  
   - `"Second Class"` (50–59)  
   - `"Pass"` (35–49)  
   - `"Fail"` (< 35)

   **Answer**
```js
let marks=87;
let result=marks<=10 && marks>=75? "Distinction": marks>=60? "First Class" : marks>=50? "Second Class" : marks>=35? "Pass" : "Fail"
console.log(result)
```

7. Write a single nested ternary expression that returns one of the following based on a number:  
   `"Positive Even"`, `"Positive Odd"`, `"Negative Even"`, `"Negative Odd"`, or `"Zero"`.

   **Answer**
```js
let num=80
let result=num>0?(num%2==0? "Positive Even" : "Positive Odd"): num<0?(num%2==0? "Negative and Even" : "Negative and Odd") :"zero";
console.log(result)
```

8. Using only nested ternary operators, implement the full leap year logic  
   (divisible by 4 **and** (not divisible by 100 **or** divisible by 400)) and return `"Leap Year"` or `"Not a Leap Year"`.

   **Answer**
```js
let year=2026
let result=year%4==0? (year%100==0? (year%400==0? "leap year" : "not a leap year") : "leap year") : "not a leap year"
console.log(result)
```

9. Convert the following decision tree into **one single nested ternary** expression:  
   ```
   if (role === "admin") {
     if (action === "delete") → "Admin Delete"
     else if (action === "edit") → "Admin Edit"
     else → "Admin Other"
   } else if (role === "user") {
     if (action === "view") → "User View"
     else → "User Restricted"
   } else {
     → "Invalid Role"
   }
   ```

   **Answer**
```js
let role = "admin"
let action = "view"
let result = role==="admin"? (action==="delete"? console.log("Admin Delete") : action==="edit"? console.log("Admin Edit") : console.log("Admin Other")) : role==="user"? (action==="view"? console.log("User View") : console.log("User Restricted")) : console.log("Invalid Role")
```

10. Write a complex nested ternary that calculates discount and final amount based on these rules:  
    - Cart total ≥ 5000 → 20% discount  
    - Cart total ≥ 2000 → 10% discount  
    - Cart total ≥ 1000 → 5% discount  
    - Otherwise → 0% discount  
    Return both the discount percentage and the final payable amount in a single expression (you may return an object or a formatted string).
    
   **Answer**
```js
let cartTotal=2500
let result=cartTotal>=5000? `final amount= ${cartTotal-cartTotal*0.20}`:cartTotal>=2000?`final amount= ${cartTotal-cartTotal*0.10}`:cartTotal>=1000?`final amount= ${cartTotal-cartTotal*0.05}`: `final amount= ${cartTotal}`
console.log(result)
```