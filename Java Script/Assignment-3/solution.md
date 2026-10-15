# Assignment : JavaScript Operators

---

## A] Arithmetic Operators

### 1. Addition `+`

1. A school collected ₹15,000 from one class and ₹12,500 from another class. Find the total collection.  

**Answer**
```javascript
let firstClassCollection = 15000;
let secondClassCollection = 12500;
let totalCollection = firstClassCollection+secondClassCollection;
console.log("Total Collection= ", totalCollection)
```

2. A person reads 18 pages in the morning and 25 pages in the evening. Find the total pages read. 

**Answer**
```javascript
let pagesReadInMorning = 18;
let pagesReadInEvening = 25;
let totalPagesRead = pagesReadInMorning+pagesReadInEvening;
console.log("Total Pages Read =", totalPagesRead)
```

3. A shop sold 125 items on Monday and 178 items on Tuesday. Find the total items sold.

**Answer**
```javascript
let itemsSoldOnMonday = 125;
let itemsSoldOnTuesday = 178;
let totalItemSold = itemsSoldOnMonday+itemsSoldOnTuesday;
console.log("Total Item Sold =", totalItemSold)
```

4. Predict the output:
   ```js
   let a = "10";
   let b = 5;
   let result = a + b;
   console.log(result);
   ```

**Answer**
output=105

5. Predict the output:
   ```js
   let x = 5;
   let y = "3";
   let result = x + y;
   console.log(result);
   ```

**Answer**
output=53

6. What is the output of `15 + 27`?

**Answer**
output=42

7. Calculate the total price if a book costs ₹350 and a pen costs ₹45. 

**Answer**
```javascript
let priceOfBook = 350;
let priceOfPen = 45;
let totalPrice = priceOfBook+priceOfPen;
console.log("Total Price =", totalPrice)
```

8. What is the result of `"25" + 10` and why?  

**Answer**
output= 2510
Reason= Because in javascript when a string and a number is added javascript first convert the number into string and then add them.

9. A person has ₹2000 in their wallet. They buy items worth ₹750 and ₹320. Write an expression using `+` to find the total spent, then calculate the remaining balance.  

**Answer**
```javascript
let priceInWallet = 2000;
let firstItemPrice = 750;
let secondItemPrice = 320;
let totalSpent = firstItemPrice+secondItemPrice;
console.log("Total spent =", totalSpent);
let remainingBalance = priceInWallet-totalSpent;
console.log("Remaining Balance= ", remainingBalance)
```

10. Predict the outputs and explain:  
    ```js
    console.log(5 + "5" + 5);
    console.log(5 + 5 + "5");
    console.log("5" + 5 + 5);
    ```

**Answer**
- output1 = 555. 
- Reason = because we always do addition from left to right so we first add '5 + "5"' and second 5 is string so answer is '"55"' them we add '"55"+5' here 55 is also a string so final answer is '"555"'
- output2 = 105
- Reason = because we first add '5+5' and both are number so answer is '10' then we add '10 + "5"' and 5 is string so final answer is 105.
- output3 = 555
- Reason = because we first add '"5"+5' and first 5 is a string so answer is '"55"' then we add '"55" + 5' and 55 is string so final answer is 555.
---

### 2. Subtraction `-`

1. A bus has 80 seats, and 53 seats are occupied. Find the number of empty seats. 
**Answer**
```javascript
let totalSeats = 80;
let occupiedSeats = 53;
let emptySeats = totalSeats-occupiedSeats;
console.log("Empty Seats= ", emptySeats)
```

2. A student has 500 marks and loses 35 marks due to incorrect answers. Find the final marks.  

**Answer**
```javascript
let totalMarks = 500;
let marksLoss = 35;
let finalmarks = totalMarks-marksLoss;
console.log("Final Marks =", finalmarks)
```

3. A warehouse has 2,500 boxes and sends 875 boxes to a store. Find the remaining boxes. 

**Answer**
```javascript
let totalBoxes = 2500;
let boxesSend = 875;
let remainingBoxes = totalBoxes-boxesSend;
console.log("Remaining Boxes =", remainingBoxes)
```

4. Predict the output:
   ```js
   let a = "10";
   let b = 3;
   let result = a - b;
   console.log(result);
   ```
   
**Answer**
Output = 7

5. Predict the output:
   ```js
   let x = "20";
   let y = "5";
   let result = x - y;
   console.log(result);
   ```
   
**Answer**
Output = 15

6. What is the output of `100 - 37`?  
   
**Answer**
Output = 63

7. A tank has 500 litres of water. After using 175 litres, how much water is left?  
   
**Answer**
```js
let amountOfWaterInTank = 500
let amountOfWaterUsed = 175
let remainingWater = amountOfWaterInTank-amountOfWaterUsed
console.log("Water left in tank= ", remainingWater)
```

8. What is the result of `"50" - 20` and `"50" - "20"`? Explain any difference.  
   
**Answer**
Output1 = 30;
Output2 = 30;
Difference =  No, there is no difference because javascript convert the string into number and then do substraction.

9. A shopkeeper had 240 apples. He sold 95 in the morning and 67 in the evening. Write expressions to find how many apples are left.  
   
**Answer**
```js
let totalApples = 240;
let applesSoldInMorning = 95;
let applesSoldInEvening = 67;
let totalApplesSold = applesSoldInMorning+applesSoldInEvening;
let remainingApples = totalApples-totalApplesSold;
console.log("Remaining Apples =", remainingApples);
```

10. Predict and explain the outputs:  
    ```js
    console.log("100" - 50);
    console.log("abc" - 10);
    console.log(10 - "5" - "2");
    console.log("10" - "5" - "2");
    ```

**Answer**
- Output1 = 50. 
- Explaination = Because javascript convert all the string into number to do sustraction and always do substraction from left to right.
- Output2 = NaN. 
- Explaination = Because when 'abc' convert into number it become 'NaN(not a number)' value so the result is also a NaN.
- Output3 = 3. 
- Explaination = Because javascript convert all the string into number to do sustraction and always do substraction from left to right.
- Output4 = 3. 
- Explaination = Because javascript convert all the string into number to do sustraction and always do substraction from left to right.
---

### 3. Multiplication `*`

1. One notebook costs ₹45. Calculate the cost of buying 8 notebooks.  

**Answer**
```js
let noOfNotebook=8
let costPerNotebook=45
let totalCost=noOfNotebook*costPerNotebook
console.log("Total cost of 8 notebook =", totalCost)
```

2. A machine produces 120 bottles per hour. Calculate its production in 6 hours.  

**Answer**
```js
let totalTime=6
let productionInOneHour=120
let productionInSixHours=totalTime*productionInOneHour
console.log("Total Production In 6 Hours=", productionInSixHours)
```

3. A garden has 7 rows with 15 plants in each row. Find the total number of plants.  

**Answer**
```js
let totalRows=6
let plantsInEachRow=15
let TotalPlants=totalRows*plantsInEachRow
console.log("Total Plants in the Garden =", TotalPlants)
```

4. Predict the output:
   ```js
   let a = "5";
   let b = 4;
   let result = a * b;
   console.log(result);
   ```

**Answer**
Output = 20

5. Predict the output:
   ```js
   let x = "10";
   let y = "2";
   let result = x * y;
   console.log(result);
   ```
   
**Answer**
Output = 20

6. What is the output of `12 * 8`?  
   
**Answer**
Output = 96

7. One pizza costs ₹299. What is the total cost of 4 pizzas? 

**Answer**
```js
let totalNoOfPizza=4
let costOfEachPizza=299
let costOf4Pizza=totalNoOfPizza*costOfEachPizza
console.log("Total cost of 4 pizza =", costOf4Pizza)
```

8. What is the result of `"7" * 6` and `"7" * "6"`?  

**Answer**
- Output1 = 42
- Output2 = 42

9. A factory produces 45 units per hour. How many units does it produce in 8 hours? Write the expression and calculate.  

**Answer**
```js
let totalTime = 8;
let productionPerHour = 45;
let totalProduction = totalTime*productionPerHour;
console.log("Total production in 8 hours =", totalProduction)
```

10. Predict and explain the outputs:  
    ```js
    console.log("5" * 3 * "2");
    console.log("abc" * 4);
    console.log(10 * "2.5");
    console.log("10" * "2.5" * "0");
    ```

**Answer**
- Output1 = 30
- Explaination = because javascript first convert all the string into number which participate in multiplication and then do multiplication from left to right.
- Output2 = NaN
- Explaination = because when we convert abc into a number it become NaN so its multiply with 4 is also a NaN.
- Output3 = 25
- Explaination = because javascript first convert all the string into number which participate in multiplication and then do multiplication from left to right so answer of '10*2.5' is '25'.
- Output4 = 0
- Explaination = because we first do '2 * 2.5' which is 25 then we do '25 * 0' which is 0.

---

### 4. Division `/`

1. A teacher distributes 144 pencils equally among 12 students. Find the number of pencils each student receives.  

**Answer**
```js
let totalPencils = 144
let totalStudents = 12
let pencilEachStudentReceive = totalPencils / totalStudents
console.log("No. of pencils each student receive =", pencilEachStudentReceive)
```

2. A train travels 360 kilometres in 6 hours. Find its average distance travelled per hour. 

**Answer**
```js
let totaldistance = 360
let totalTime = 6
let averageSpeed = totaldistance / totalTime
console.log("Average speed of train =", averageSpeed)
```

3. A company distributes ₹72,000 equally among 9 departments. Find the amount received by each department.  

**Answer**
```js
let totalAmount = 72000
let totalDepartment = 9
let amountEachDepartmentReceive = totalAmount / totalDepartment
console.log("Amount each departent receives =", amountEachDepartmentReceive)
```

4. Predict the output:
   ```js
   let a = "20";
   let b = 4;
   let result = a / b;
   console.log(result);
   ```
   
**Answer**
Output= 5

5. Predict the output:
   ```js
   let x = "100";
   let y = "5";
   let result = x / y;
   console.log(result);
   ```
   
**Answer**
Output= 10

6. What is the output of `144 / 12`?  

**Answer**
Output= 12

7. 360 students are to be divided equally into 9 classrooms. How many students per classroom?  

**Answer**
```js
let totalStudents = 360
let totalClassrooms = 9
let studentInEachClassroom = totalStudents / totalClassrooms
console.log("No. of students in each classroom =", studentInEachClassroom)
```

8. What is the result of `"100" / 4` and `"100" / "4"`?  

**Answer**
Output1= 25
Output2= 25

9. A total bill of ₹2400 is to be shared equally among 6 friends. Write the expression and find each person’s share.  

**Answer**
```js
let totalBill = 2400
let totalFriend = 6
let eachPersonShare = totalBill / totalFriend
console.log("Each person share =", eachPersonShare)
```

10. Predict and explain the outputs:  
    ```js
    console.log(10 / 0);
    console.log(-10 / 0);
    console.log(0 / 0);
    console.log("20" / "4" / 2);
    console.log("abc" / 5);
    ```
    
**Answer**
- Output1= Infinity
- Explaination= If any number divided by Zero then the result will be infinite.
- Output2= -Infinity
- Explaination= If a negative number divided by Zero then the result will be -infinite.
- Output3= NaN
- Explaination= 
- Output4= 2.5
- Explaination= javascript convert all the strings into number which participate in division so we first do '20/5' which is 5 then '5/2' which is '2.5' .
- Output5= NaN
- Explaination= as 'abc' cannot convert into number it become NaN type number so the division result is also a NaN.

---

### 5. Modulus `%`

1. A teacher has 53 students and forms groups of 5. Find the number of students left over.  

**Answer**
```js
let noOfStudents = 53;
let studentInEachGroup = 5;
let studentLeftOver = noOfStudents % studentInEachGroup
console.log("Student left over =", studentLeftOver)
```

2. A shop has 128 candies and packs 10 candies in each box. Find the number of candies left unpacked.  

**Answer**
```js
let totalCandies = 128;
let candiesInEachBox = 10
let candiesleft = totalCandies % candiesInEachBox
console.log("Number of candies left unpacked =", candiesleft)
```

3. A factory produces 237 toys and packs them in boxes of 6. Find how many toys are left after packing full boxes.  

**Answer**
```js
let toysProduces = 237
let toysInEachBox = 6
let toysLeft = toysProduces % toysInEachBox
console.log("Number of Toys left after packing full boxes =", toysLeft)
```

4. A bus can carry 40 passengers. If 185 people are waiting, find how many people will be left after filling as many full buses as possible.  

**Answer**
```js
let capacityofBus = 40
let peopleWaiting = 185
let peopleLeft = peopleWaiting % capacityofBus
console.log("Number of people left after filling as many full buses =", peopleLeft)
```

5. Predict the output:
   ```js
   let a = 10;
   let b = 0;
   let result = a % b;
   console.log(result);
   ```

**Answer**
Output = NaN

6. What is the output of `29 % 5`?  

**Answer**
Output = 4

7. There are 23 chocolates to be packed in boxes of 4. How many chocolates will be left over?  

**Answer**
- Answer = 3 Chocolates left over

8. What is the result of `0 % 7` and `15 % 0`? Explain.  

**Answer**
- Output1 = 0
- Explaination = if '0' divided by any number then the remainder and result will always be '0'.
- Output2 = NaN
- Explaination = if any number divided by '0' then the result will be infinite so we will not get remainder that's why the answer is NaN.

9. A number of pages (47) needs to be printed on sheets that hold 6 pages each. How many full sheets are needed and how many pages will be left over? Write expressions using `%` and `/`.  

**Answer**
```js
let totalpages = 47;
let pagesOnEachSheet = 6;
let totalFullSheetsRequired = totalpages / pagesOnEachSheet
let pagesLeftOver = totalpages % pagesOnEachSheet
console.log("Number of full sheets required =", Math.floor(totalFullSheetsRequired));
console.log("Number of pages left over =", pagesLeftOver);
```

10. Predict and explain the outputs (especially the signs):  
    ```js
    console.log(17 % 5);
    console.log(-17 % 5);
    console.log(17 % -5);
    console.log(-17 % -5);
    console.log(10 % 0);
    ```
    
**Answer**
- Output1 = 2
- Explaination = here we simply find the remainder of '17/5' which is 2.
- Output2 = -2
- Explaination = if one number is positive and other is negative then  javascript will take the sign of bigger number.
- Output3 = 2
- Explaination = if one number is positive and other is negative then  javascript will take the sign of bigger number.
- Output4 = -2
- Explaination = here the answer is -2 because if both the number in modules oppression is negative then javascript will make the answer negative also.
- Output5 = NaN
- Explaination = if any number divided by '0' then the result will be infinite so we will not get remainder that's why the answer is NaN.

---

### 6. Exponentiation `**`

1. Find the volume of a cube with a side length of 6 cm using `side ** 3`.  

**Answer**
```js
let side = 6
let volumeOfCube = side**3
console.log("Volume of Cube =", volumeOfCube)
```

2. Calculate the total number of cells in a square arrangement with 9 cells on each side using `side ** 2`.  

**Answer**
```js
let side = 9
let totalCells = side**2
console.log("Total no. of cells on each side =", totalCells)
```

3. Find the value of \( 5^4 \) (5 raised to the power 4) using the exponentiation operator.  

**Answer**
```js
console.log(5**4)
```

4. A digital image has 1,024 pixels on each side (square image). Find the total number of pixels using `pixels ** 2`.  

**Answer**
```js
let pixels = 1024
let totalNoOfPixels = pixels**2
console.log("Total no. of pixels =", totalNoOfPixels)
```

5. Predict the output:
   ```js
   let base = 2;
   let power = -1;
   let result = base ** power;
   console.log(result);
   ```
   
**Answer**
Output = 0.5

6. What is the output of `3 ** 4`?  

**Answer**
Output = 81

7. Calculate the area of a square whose side is 9 units using the exponentiation operator.  

**Answer**
```js
let side = 9
let area = side**2
console.log("Area of square =", area)
```

8. What is the result of `2 ** 5` and `5 ** 2`? Are they the same?  

**Answer**
- Output1 = 32.
- Output2 = 25.
- No, they are not same.

9. Predict and explain the outputs (and any errors):  
   ```js
   console.log(2 ** 3 ** 2);          // right-associative
   console.log((2 ** 3) ** 2);
   console.log(2 ** -3);
   // console.log(-2 ** 2);           // Remember: Syntax error
   console.log((-2) ** 2);
   console.log(4 ** 0.5);
   ```
   
**Answer**
Output1 = 512
Explaination = in exponentiation oppresion we do oppression from right to left. so we first do '3**2' which is 9 then we will do '2**9' which is 512.
Output2 = 64
Explaination = here we first solve the backet which is '8' then we will do '8**2' which is 64.
Output3 = 0.125
Explaination = here the power of '2' is '-3' so we will first do '2**3' which is 8 then we devide 1 by 8 which is '0.125'.
Output4 = 4
Explaination = here we multiply '-2' with '-2' so both '-' will combine and form '+' and '2*2' will form 4 so answer is 4.
Output5 = 2
Explaination = here the power of '4' is '0.5' so we need to half the value '4' and the half of 4 is 2.

10. Predict the output:
    ```js
    let a = 10;
    let b = 0;
    let result = a ** b;
    console.log(result);
    ```

**Answer**
Output = 1


---

## B] Assignment Operators

### 1. Simple Assignment `=`
1. Store a student’s name as `"Priya"` and marks as `92` using the assignment operator.  

**Answer**
```js
let studentName = "Priya"
let marks = 92
```

2. Create a variable `score` and assign it the value `0`.  

**Answer**
```js
let score = 0
```

3. Assign the value `50` to three variables `a`, `b` and `c` using a single chained assignment.  

**Answer**
```js
let a = b = c = 50
```

4. Predict the output:
   ```js
   let x;
   x = 100;
   console.log(x);
   ```

**Answer**
- Output = 100

5. Predict the output:
   ```js
   let p = 15;
   let q = p;
   q = 30;
   console.log(p, q);
   ```

   **Answer**
- Output = 15 30

---

### 2. Add and Assign `+=`
1. A player’s score is `80`. He scores `25` more points. Update the score using `+=`.  

**Answer**
```js
let score = 80
score += 25
```

2. A wallet has ₹1500. Cashback of ₹120 is added. Update the balance using `+=`.  

**Answer**
```js
let balance = 1500
balance += 120
```

3. Predict the output:
   ```js
   let count = 10;
   count += 5;
   console.log(count);
   ```
   
   **Answer**
- Output = 15

4. Predict the output:
   ```js
   let msg = "Good";
   msg += " Morning";
   console.log(msg);
   ```
      
   **Answer**
- Output = Good Morning

5. What is the final value after `let n = 20; n += "5";`? Explain.

**Answer**
- final value = 205
- Explaination = answer is 205 because we first assign n as 20 which is a number then we add "5" which is a string so javascript will convert 20 into a string then add them so it will become 205.

---

### 3. Subtract and Assign `-=`
1. Health is `100`. Player takes `35` damage. Update health using `-=`.  

**Answer**
```js
let health = 100
health -= 35
```

2. Stock of 300 items is reduced by 45 after a sale. Update using `-=`.  

**Answer**
```js
let stock = 300
stock -= 45
```

3. Predict the output:
   ```js
   let lives = 5;
   lives -= 2;
   console.log(lives);
   ```
      
   **Answer**
- Output = 3

4. Predict the output:
   ```js
   let num = "40";
   num -= 15;
   console.log(num);
   ```
      
**Answer**
- Output = NaN

5. What is the result of `let x = "abc"; x -= 5;`? Explain.

   **Answer**
- Result = NaN
- explaination = here we assign x as "abc" which is a string then we substract 5 from it which is a number so javascript will convert abc into number and it will become NaN And if we substract any number from NaN the result will always be NaN.

---

### 4. Multiply and Assign `*=`
1. Price of an item is ₹500. Apply 18% GST using `*= 1.18`.  

**Answer**
```js
let price = 500
price *= 1.18
```

2. A quantity of 8 is tripled. Update using `*=`.  

**Answer**
```js
let quantity = 8
quantity *= 3
```

3. Predict the output:
   ```js
   let amount = 200;
   amount *= 1.1;
   console.log(amount);
   ```
         
**Answer**
- Output = 220

4. Predict the output:
   ```js
   let val = "7";
   val *= 3;
   console.log(val);
   ```
            
**Answer**
- Output = 21

5. What is the result of `let y = "hello"; y *= 2;`? Explain.

   **Answer**
- Result = NaN
- explaination = here we assign y as "hello" which is a string then we multiply 2 in it which is a number so javascript will convert 'Hello' into number and it will become NaN and if we multiply anynumber from NaN the result will always be NaN.

---

### 5. Divide and Assign `/=`
1. Total of 180 chocolates is shared among 6 children. Update using `/=`.  

**Answer**
```js
let chocolates = 180
chocolates /= 6
```

2. Distance of 300 km is covered in 5 hours. Find average speed using `/=`.  

**Answer**
```js
let distance = 300
distance /= 5
```

3. Predict the output:
   ```js
   let total = 400;
   total /= 8;
   console.log(total);
   ```
            
**Answer**
- Output = 50

4. Predict the output:
   ```js
   let num = "100";
   num /= 4;
   console.log(num);
   ```
            
**Answer**
- Output = 25

5. What is the result of `let z = 50; z /= 0;`? Explain.

**Answer**
- result = infinity
- explaination = here z assign as 50 then we divide it from 0  and if any number divide by 0 then the result will be infinity.

---

### 6. Modulus and Assign `%=`
1. Number 47 is divided by 6. Store only the remainder using `%=`.  

**Answer**
```js
let number = 47
number %= 6
```

2. Counter is at 23. Keep only the remainder when divided by 12 using `%=`.  

**Answer**
```js
let counter = 23
counter %= 12
```

3. Predict the output:
   ```js
   let num = 29;
   num %= 5;
   console.log(num);
   ```
            
**Answer**
- Output = 4

4. Predict the output:
   ```js
   let x = "17";
   x %= 3;
   console.log(x);
   ```
            
**Answer**
- Output = 2

5. What is the result of `let m = 15; m %= 0;`? Explain.

**Answer**
- result = NaN
- explaination = here m assign as 15 then we divide it from 0  and if any number divide by 0 then the result will be infinity so we will not get the remainder that's why the result will become NaN.

---

### 7. Exponentiation and Assign `**=`
1. Side of a cube is 5. Update it to get the volume using `**= 3`.  

**Answer**
```js
let side = 5
side **= 3
```

2. Number 4 needs to be squared. Use `**= 2`.  

**Answer**
```js
let number = 4
number **= 2
```

3. Predict the output:
   ```js
   let base = 2;
   base **= 5;
   console.log(base);
   ```
            
**Answer**
- Output = 32

4. Predict the output:
   ```js
   let n = 4;
   n **= 0.5;
   console.log(n);
   ```
            
**Answer**
- Output = 2

5. What is the result of `let p = 2; p **= -1;`? Explain.

**Answer**
- Output = 0.5
- explaination = if any number power is '-' then it means after exponent happen it divided 1 it means the expresion will become "1/(2**1)" 
so later the expression will become "1/2" which is '0.5'.

---

## C] Comparison Operators

### 1. Loose Equality `==`
1. Check whether the string `"25"` is loosely equal to the number `25`.  

**Answer**
- Output = true

2. Check if `0 == false` returns true or false.  

**Answer**
- Output = true

3. Predict the output:
   ```js
   console.log(10 == "10");
   console.log(null == undefined);
   ```
            
**Answer**
- Output = true

4. Predict the output:
   ```js
   console.log("" == 0);
   console.log([] == false);
   ```
            
**Answer**
- Output1 = true
- Output2 = true

5. Why does `NaN == NaN` return `false`?

**Answer**
- explaination = because NaN is not equal to anything, including itself.

---

### 2. Loose Inequality `!=`
1. Check whether `"18" != 18` returns true or false.  

**Answer**
- Output = false

2. A password is stored as `"1234"`. User enters `1234` (number). Will `!=` return true?  

**Answer**
- Output = false

3. Predict the output:
   ```js
   console.log(5 != "5");
   console.log(0 != false);
   ```
               
**Answer**
- Output1 = false
- Output2 = flase

4. Predict the output:
   ```js
   console.log(null != undefined);
   console.log("" != 0);
   ```
               
**Answer**
- Output1 = false
- Output2 = flase

5. What does `NaN != NaN` return? Explain.

**Answer**
- Result = true
- explaination = because NaN is not equal to anything, including itself.

---

### 3. Strict Equality `===`
1. Check whether `"25" === 25` returns true or false. Explain why.  

**Answer**
Output = False
- explaination = because '===' sign check both value and type and here first 25 is string and second 25 is number that's why the output return false.

2. Check if `0 === false` and `null === undefined`.  

**Answer**
- Output1 = false
- Output2 = false

3. Predict the output:
   ```js
   console.log(10 === "10");
   console.log(true === 1);
   ```
               
**Answer**
- Output1 = false
- Output2 = false

4. Predict the output:
   ```js
   console.log("" === 0);
   console.log([] === false);
   ```
               
**Answer**
- Output1 = false
- Output2 = false

5. Why is `===` preferred over `==` in most real-world code?

**Answer**
- Explaination = because '===' check two things type and value  and "==" checks only value.

---

### 4. Strict Inequality `!==`
1. Check whether `"18" !== 18` returns true or false.  

**Answer**
- Output = true

2. Check if `0 !== false` and `null !== undefined`.  

**Answer**
- Output1 = true
- Output2 = true

3. Predict the output:
   ```js
   console.log(5 !== "5");
   console.log(true !== 1);
   ```
               
**Answer**
- Output1 = true
- Output2 = true

4. Predict the output:
   ```js
   console.log("" !== 0);
   console.log(NaN !== NaN);
   ```
               
**Answer**
- Output1 = true
- Output2 = true

5. Write a condition that checks if a variable `input` is strictly not equal to the string `"0"`.

**Answer**
```js
let input;
console.log(input !== "0")
```

## Part D] Relational Operator

### 5. Greater Than `>`
1. A student’s marks are 78. The passing marks are 40. Check whether the student has scored more than the passing marks.  

**Answer**
```js
let studentMarks = 78
let passingMarks = 40
let isStudentPass = studentMarks > passingMarks
console.log(isStudentPass)
```

2. Temperature today is 35°C and yesterday it was 28°C. Check if today is hotter.  

**Answer**
```js
let todaysTemperature = 35
let yesterdaysTemperature = 28
let isTemperatureIncrease = todaysTemperature > yesterdaysTemperature
console.log(isTemperatureIncrease)
```

3. Predict the output:
   ```js
   console.log(15 > 10);
   console.log(10 > 15);
   console.log(10 > 10);
   ```

**Answer**
- Output1 = true
- Output2 = false
- Output3 = false

4. Predict the output:
   ```js
   console.log("20" > 15);
   console.log("5" > "10");
   console.log("abc" > 10);
   ```
   
**Answer**
- Output1 = true
- Output2 = true
- Output3 = false

5. What is the result of `null > 0` and `undefined > 0`? Explain.  

**Answer**
- result1 = false
- result2 = false
- explaination = if we convert null into number it become 0 means null is not greater than 0 it is equal to 0 and second if we convert undefined into number it becone NaN and NaN is neither greater than, equal or less than any number so result will always be false.

6. A shop has 120 items in stock. A customer wants to buy 85 items. Write a condition using `>` to check if stock is sufficient.  

**Answer**
```js
let itemStock = 120
let itemWant = 85
let isStockSufficient = itemStock > itemWant
console.log(isStockSufficient)
```

7. Predict and explain:
   ```js
   console.log(true > false);
   console.log("10" > "2");
   console.log(NaN > 5);
   ```
   
**Answer**
- Output1 = true     (Because number value of false is 0 and true is 1.)
- Output2 = false    (Because if we perform relational operator on two strings it will compare the unicode value of first digit if first first digit is same then it will go to next digit)
- Output3 = false    (Because if we compare NaN with any number and with any Relational operator result will always be false)


### 6. Less Than `<`
1. A box can hold maximum 50 kg. Current weight is 42 kg. Check if more items can still be added.  

**Answer**
```js
let currentWeight = 42
let maxWeightLimit = 50
let isItemAdded = currentWeight < maxWeightLimit
console.log(isItemAdded)
```

2. Age of a person is 16. Minimum age required is 18. Check if the person is underage.  

**Answer**
```js
let personAge = 16
let minAgeRequired = 18
let isPersonUnderage = personAge < minAgeRequired
console.log(isPersonUnderage)
```

3. Predict the output:
   ```js
   console.log(8 < 12);
   console.log(20 < 10);
   console.log(7 < 7);
   ```
   
**Answer**
- Output1 = true
- Output2 = false
- Output3 = false

4. Predict the output:
   ```js
   console.log("8" < 10);
   console.log("20" < "3");
   console.log("hello" < 5);
   ```
      
**Answer**
- Output1 = true
- Output2 = true
- Output3 = false

5. What is the result of `null < 0` and `undefined < 0`? Explain.  

**Answer**
- result1 = false
- result2 = false
- explaination =  if we convert null into number it become 0 means null is not less than 0 it is equal to 0. Second if we convert undefined into number it becone NaN and NaN is neither greater than, equal or less than any number so result will always be false.

6. A tank capacity is 500 litres. Current water level is 375 litres. Write a condition using `<` to check if it is not full.  

**Answer**
```js
let tankCapacity = 500
let currentWaterLevel = 375
let isTankFull = tankCapacity < currentWaterLevel
console.log("Is TankFull=", isTankFull)
```

7. Predict and explain:
   ```js
   console.log(false < true);
   console.log("5" < "15");
   console.log(NaN < 10);
   ```
      
**Answer**
- Output1 = true     (Because number value of false is 0 and true is 1.)
- Output2 = false    (Because if we perform relational operator on two strings it will compare the unicode value of first digit if first first digit is same then it will go to next digit)
- Output3 = false    (Because if we compare NaN with any number and with any Relational operator result will always be false)


### 7. Greater Than or Equal To `>=`
1. Minimum marks required for distinction is 75. A student scored 75. Check if the student gets distinction.  

**Answer**
```js
let minMarksForDistinction = 75
let studentScored = 75
let isStudentGetDistinction = studentScored >= minMarksForDistinction
console.log("Is student get distincton=", isStudentGetDistinction)
```

2. Ticket price is ₹300. A person has ₹300. Check if they can buy the ticket.  

**Answer**
```js
let ticketPrice = 300
let moneyPersonHave = 300
let areTheyCanBuyTicket = moneyPersonHave >= ticketPrice
console.log("Is they can buy ticket=", areTheyCanBuyTicket)
```

3. Predict the output:
   ```js
   console.log(25 >= 25);
   console.log(30 >= 25);
   console.log(20 >= 25);
   ```
      
**Answer**
- Output1 = true
- Output2 = true
- Output3 = false

4. Predict the output:
   ```js
   console.log("25" >= 25);
   console.log("10" >= "2");
   console.log(null >= 0);
   ```
      
**Answer**
- Output1 = true
- Output2 = false
- Output3 = true

5. What is the result of `undefined >= 0`? Explain.  

**Answer**
- Result = false
- explaination =  if we convert undefined into number it becone NaN and NaN is neither greater than, equal or less than any number so result will always be false.

6. A lift can carry maximum 8 people. Currently 8 people are inside. Write a condition using `>=` to check if the lift is full or overloaded.  

**Answer**
```js
let maxPeopleCapacity = 8
let currentPeopleInside = 8
let isLiftFull = currentPeopleInside >= maxPeopleCapacity
console.log("Is lift full or overload=", isLiftFull)
```

7. Predict and explain:
   ```js
   console.log(true >= 1);
   console.log("" >= 0);
   console.log(NaN >= NaN);
   ```
      
**Answer**
- Output1 = true     (Because the number value of true is 1)
- Output2 = true     (Because if a string is empty its number value is 0)
- Output3 = false    (Because NaN is not greater than, less than or equal to anymthing include itself)


### 8. Less Than or Equal To `<=`
1. Maximum speed limit is 60 km/h. A vehicle is travelling at 60 km/h. Check if it is within the limit.  

**Answer**
```js
let maxSpeedLimit = 60
let vehicleSpeed = 60
let isItWithinLimit = vehicleSpeed <= maxSpeedLimit
console.log("Is it within limit=", isItWithinLimit)
```

2. A student needs at least 40 marks to pass. He scored 39. Check if he has failed.  

**Answer**
```js
let minMarks = 40
let studentScored = 39
let isHeFailed = studentScored <= minMarks
console.log("Is he failed=", isHeFailed)
```

3. Predict the output:
   ```js
   console.log(15 <= 20);
   console.log(20 <= 15);
   console.log(15 <= 15);
   ```
      
**Answer**
- Output1 = true
- Output2 = false
- Output3 = true

4. Predict the output:
   ```js
   console.log("15" <= 20);
   console.log("30" <= "5");
   console.log(null <= 0);
   ```
      
**Answer**
- Output1 = true
- Output2 = true
- Output3 = true

5. What is the result of `undefined <= 0`? Explain.  

**Answer**
- Result = false
- explaination =  if we convert undefined into number it becone NaN and NaN is neither greater than, equal or less than any number so result will always be false.

6. A bag can hold maximum 10 books. Currently it has 10 books. Write a condition using `<=` to check if more books can be added.  

**Answer**
```js
let bagCapacity = 10
let currentBooksInside = 10
let isBagFull = bagCapacity <= currentBooksInside
console.log("Is bag full or overload=", isBagFull)
```

7. Predict and explain:
   ```js
   console.log(false <= 0);
   console.log("" <= 0);
   console.log(NaN <= 5);
   ```
      
**Answer**
- Output1 = true     (Because the number value of false is 0)
- Output2 = true     (Because if a string is empty its number value is 0)
- Output3 = false    (Because if we compare NaN with any number and with any Relational operator result will always be false)


### Mixed Practice (>, <, >=, <=)
1. Write expressions to check:
   - Whether age `18` is greater than or equal to voting age `18`.
      
**Answer**
```js
let age = 18
let votingAge = 18
console.log(age >= votingAge)
```

   - Whether temperature `32` is less than `35`.
      
**Answer**
```js
let temperature = 32
console.log(temperature < 35)
```

   - Whether score `90` is greater than `85`.
   
**Answer**
```js
let score = 90
console.log(score > 85)
```

2. Predict the outputs:
   ```js
   console.log(10 > 5 && 5 < 10);
   console.log("10" >= 10);
   console.log(null <= undefined);
   console.log("5" < "10" && 5 > 2);
   ```
      
**Answer**
- Output1 = true
- Output2 = true
- Output3 = false
- Output4 = false

3. A product costs ₹499. A customer has ₹500. Write conditions using `>=` and `<` to decide if the customer can buy it and if any change will be left.  

**Answer**
```js
let productCost = 499
let moneyCustomerHave = 500
let isCustomerCanBuyIt = moneyCustomerHave >= productCost
let isChangeLeft = productCost < moneyCustomerHave
console.log("Is Customer can Buy it=", isCustomerCanBuyIt)
console.log("Is Change left=", isChangeLeft)
```

4. Explain why `"10" > "2"` is `false` but `10 > 2` is `true`.
   
**Answer**
- Explaination = Because if we perform relational operator on two strings it will compare the unicode value of both string first digit if first digit is same then it will go to next digit

## Part E]: Increment / Decrement Operators (`++` / `--`)

### Part a:

1. A counter starts at `5`. Use the increment operator to increase it by 1 and print the new value.  

**Answer**
```js
let a=5;
a++;
console.log(a)
```

2. A player has `3` lives. Use the decrement operator to reduce one life and print the remaining lives. 

**Answer**
```js
let lives=3;
lives--;
console.log("Remaining lives=", lives)
```

3. Start with `score = 10`. Increase the score using `++` and print it.  

**Answer**
```js
let score=10;
score++;
console.log("Score=", score)
```

4. Start with `items = 8`. Decrease the items using `--` and print it.  

**Answer**
```js
let items = 8;
items--;
console.log("Items=", items)
```

5. Declare `count = 0`. Increment it twice and print the final value.

**Answer**
```js
let count = 0;
count++;
count++;
console.log("Count=", count)
```

### Part b:

6. Start with `x = 5`.  
   - Create `y = x++`  
   - Print both `x` and `y`.  
   Explain why the values are different.
   
**Answer**
```js
let x = 5;
let y= x++;
console.log(x)
console.log(y)
```
- Explaination=it is a edge case in python. It is known as postfix increament here we first give the value of x to y and then increament x by 1.

7. Start with `a = 5`.  
   - Create `b = ++a`  
   - Print both `a` and `b`.  
   Explain the difference from the previous question.
   
**Answer**
```js
let a = 5;
let b= ++a;
console.log(a)
console.log(b)
```
- Explaination=it is a edge case in python. It is known as prefix increament here we first increament a by 1 and then give it to b.

8. Start with `lives = 3`.  
   - Use post-decrement (`lives--`) and store the result in `previousLives`.  
   - Print both variables.
   
**Answer**
```js
let lives = 3;
let previousLives= lives--;
console.log(lives)
console.log(previousLives)
```

9. Start with `attempts = 0`.  
   - Use pre-increment (`++attempts`) and store the result in `currentAttempts`.  
   - Print both variables.

**Answer**
```js
let attempts = 0;
let currentAttempts= ++attempts;
console.log(attempts)
console.log(currentAttempts)
```

10. Start with `points = 100`.  
    - Increase it using `++`  
    - Then decrease it using `--`  
    - Print the final value.

**Answer**
```js
let points = 100;
points++;
points--;
console.log(points)
```

### Part c:

11. Predict the output:
    ```js
    let x = 10;
    let y = x++;
    let z = ++x;
    console.log(x, y, z);
    ```

    **Answer**
    - Output = 12 10 12

12. Predict the output:
    ```js
    let a = 5;
    let b = a-- + ++a;
    console.log(a, b);
    ```

    **Answer**
    - Output = 5 10

13. Predict the output:
    ```js
    let m = 7;
    let n = --m + m++;
    console.log(m, n);
    ```

    **Answer**
    - Output = 7 12

14. Predict the output:
    ```js
    let p = 3;
    let q = p++ + ++p + p;
    console.log(p, q);
    ```

    **Answer**
    - Output = 5 13

15. Predict the output:
    ```js
    let val = 0;
    val = val++ + ++val;
    console.log(val);
    ```

    **Answer**
    - Output = 2

---


## Part F]: Logical Operators

***

### 1. Logical AND `&&`

Write a JavaScript program for each:

1. Stored username is `"admin"` and password is `1234`. Check if both are valid using `&&` and print the result.  

**Answer**
```js
let storedUsername = "admin"
let storedPassword = 1234
let username = "admin"
let password = 1234
let areBothValid = username==storedUsername && password==storedPassword
console.log("Are both Valid:", areBothValid)
```

2. A user is logged in (`isLoggedIn = true`) and has permission (`hasPermission = true`). Check if they can access a page using `&&`.  

**Answer**
```js
let isLoggedIn = true
let hasPermission = true
let theyCanAccess = isLoggedIn && hasPermission
console.log("They can access the page:", theyCanAccess)
```

3. A product is in stock (`inStock = true`) and its price is less than ₹1000 (`price = 800`). Check if it can be bought using `&&`.  

**Answer**
```js
let inStock = true
let price = 800
let canItBeBought = inStock && price<1000
console.log("is it can be bought:", canItBeBought)
```

4. A student has marks `75` and attendance `80`. Passing requires marks greater than `65` **and** attendance greater than `70`. Check using `&&

**Answer**
```js
let marks = 75
let attendance = 80
let isStudentPass = marks>65 && attendance>70
console.log("is Student pass:", isStudentPass)
```
`.  
5. Two conditions: `isWeekend = true` and `isHoliday = false`. A party happens only if both are true. Check using `&&`.

**Answer**
```js
let isWeekend = true
let isHoliday = false
let isPartyHappen = isWeekend && isHoliday
console.log("is Party happens:", isPartyHappen)
```

### Additional Questions (Logical AND `&&`)

6. Predict the output:
   ```js
   let a = 0;
   let b = 10;
   let result = a && b;
   console.log(result);
   ```
   
**Answer**
- Output= 0

7. Predict the output:
   ```js
   let x = 5;
   let y = 10;
   let result = (x > 3 && y) || 0;
   console.log(result);
   ```
      
**Answer**
- Output= 10

8. Predict the output:
   ```js
   let p = "Hello";
   let q = "";
   let r = "World";
   let result = p && q && r;
   console.log(result);
   ```
      
**Answer**
- Output= 

9. Predict the output:
   ```js
   let val = 5;
   let condition = val && (val = 0);
   console.log(condition);
   console.log(val);
   ```

**Answer**
- Output1= 0
- Output2= 0

10. Predict the output:
    ```js
    let x = 10;
    let y = 20;
    let result = (x && y) && (x > y);
    console.log(result);
    ```
       
**Answer**
- Output= false


***

### 2. Logical OR `||`

Write a JavaScript program for each:

1. A user can login with either a correct password (`passwordCorrect = true`) or a valid OTP (`otpValid = false`). Check if login is allowed using `||`.  

**Answer**
```js
let passwordCorrect = true
let otpValid = false
let isLoginAllowed = passwordCorrect || otpValid
console.log("Login is Allowed:", isLoginAllowed)
```

2. A discount applies if the user is a member (`isMember = false`) or has a coupon (`hasCoupon = true`). Check using `||`.  

**Answer**
```js
let isMember = false
let hasCoupon = true
let isDiscountApplied = isMember || hasCoupon
console.log("Discount is Applied:", isDiscountApplied)
```

3. Entry is allowed if age is above `18` (`age = 16`) **or** height is above `150` cm (`height = 155`). Check using `||`.  

**Answer**
```js
let age = 16
let height = 155
let isEntryAllowed = age>18 || height>150
console.log("Entry is Allowed:", isEntryAllowed)
```

4. A form is valid if either email is given (`emailGiven = true`) or phone is given (`phoneGiven = false`). Check using `||`.  

**Answer**
```js
let emailGiven = true
let phoneGiven = false
let isFormValid = emailGiven || phoneGiven
console.log("Form is valid:", isFormValid)
```

5. A game level opens if score is above `1000` (`score = 900`) **or** time bonus is collected (`timeBonus = true`). Check using `||`.

**Answer**
```js
let score = 900
let timeBonus = true
let gameLevelOpen = score>1000 || timeBonus
console.log("is Game Level Opens:", gameLevelOpen)
```

### Additional Questions (Logical OR `||`)

6. Predict the output:
   ```js
   let a = 0;
   let b = false;
   let c = "";
   let d = null;
   let e = 42;
   let result = a || b || c || d || e;
   console.log(result);
   ```
      
**Answer**
- Output= 42

7. Predict the output:
   ```js
   let x = "Hello" || 0;
   let y = 0 || "Hi";
   console.log(x, y);
   ```
      
**Answer**
- Output= Hello Hi

8. Predict the output:
   ```js
   let a = 10;
   let b = 20;
   let result = (a < 5) || (b > 15);
   console.log(result);
   ```
      
**Answer**
- Output= true

9. Predict the output:
   ```js
   let val = 5;
   let condition = val || (val = 0);
   console.log(condition);
   console.log(val);
   ```
      
**Answer**
- Output1= 5
- Output2= 5

10. Predict the output:
    ```js
    let x = "" || 0 || false || null || undefined || "OK";
    console.log(x);
    ```
       
**Answer**
- Output= OK


***

### 3. Logical NOT `!`

Write a JavaScript program for each:

1. A user is not banned (`isBanned = false`). Check if they can login by negating `isBanned` using `!`.  

**Answer**
```js
let isBanned = false
let areTheyCanLogin=!isBanned
console.log("They can Login:", areTheyCanLogin)
```

2. A task is not completed (`isCompleted = false`). Check if it is still pending using `!`.  

**Answer**
```js
let isCompleted = false
let isItStillPending=!isCompleted
console.log("it is Still pending:", isItStillPending)
```

3. A light is on (`isOn = true`). Check if it is off using `!`.  

**Answer**
```js
let isOn = true
let isItOff=!isOn
console.log("it is Off:", isItOff)
```

4. A subscription is not active (`isActive = false`). Check if the user cannot access premium content using `!`.  

**Answer**
```js
let isActive = false
let isItCannotAccess=!isActive
console.log("is user cannot access premium content:", isItCannotAccess)
```

5. A file is not read‑only (`isReadOnly = false`). Check if it can be edited using `!`.

**Answer**
```js
let isReadOnly = false
let isItCanBeEdited=!isReadOnly
console.log("is it can be edited:", isItCanBeEdited)
```

### Additional Questions (Logical NOT `!`)

6. Predict the output:
   ```js
   let a = 0;
   let b = 1;
   console.log(!a, !b);
   ```
      
**Answer**
- Output= true false

7. Predict the output:
   ```js
   let x = "Hello";
   let y = "";
   console.log(!x, !y);
   ```
      
**Answer**
- Output= false true

8. Predict the output:
   ```js
   let val = 5;
   let result = !val;
   console.log(result);
   ```
      
**Answer**
- Output= false

9. Predict the output:
   ```js
   let a = 10;
   let b = 20;
   let result = !(a && b);
   console.log(result);
   ```
      
**Answer**
- Output= false

10. Predict the output:
    ```js
    let x = 0;
    let y = 1;
    let result = !(x || y);
    console.log(result);
    ```
       
**Answer**
- Output= false

***

---

## Part G]: `typeof` Operator
----
### Part a: 

1. Declare a variable `name = "Rahul"` and print its type using `typeof`.  

**Answer**
```js
let name = "Rahul"
console.log(typeof(name))
```

2. Declare a variable `age = 25` and print its type.  

**Answer**
```js
let age = 25
console.log(typeof(age))
```

3. Declare a variable `isStudent = true` and print its type.  

**Answer**
```js
let isStudent = true
console.log(typeof(isStudent))
```

4. Declare a variable `city` (without assigning a value) and print its type.  

**Answer**
```js
let city;
console.log(typeof(city))
```

5. Print the type of the value `null`.

**Answer**
```js
console.log(typeof(null))
```


### Part b:

6. Predict the output:
   ```js
   console.log(typeof 42);
   console.log(typeof "Hello");
   console.log(typeof true);
   console.log(typeof undefined);
   ```

   **Answer**
   - Output1 = number
   - Output2 = string
   - Output3 = boolean
   - Output4 = undefined

7. Predict the output:
   ```js
   console.log(typeof null);
   console.log(typeof {});
   console.log(typeof []);
   ```
   
   **Answer**
   - Output1 = object
   - Output2 = object
   - Output3 = object

8. Predict the output:
   ```js
   console.log(typeof NaN);
   console.log(typeof Infinity);
   console.log(typeof function(){});
   ```

   **Answer**
   - Output1 = number
   - Output2 = number
   - Output3 = function

9. Create three variables:
   - `price = 99.99`
   - `message = "Welcome"`
   - `isActive = false`  
   Print the type of each variable with a clear message.

   **Answer**
   ```js
   let price = 99.99
   let message = "Welcome"
   let isActive = false
   console.log(typeof(price))      // it is a number.
   console.log(typeof(message))    // it is a string.
   console.log(typeof(isActive))   // it is a boolean.
   ```

10. Predict the output:
    ```js
    let value = null;
    console.log(typeof value);
    console.log(typeof value === "object");
    ```

   **Answer**
   - Output1 = object
   - Output2 = true

### Part c:

11. Predict the output:
    ```js
    console.log(typeof typeof 100);
    console.log(typeof typeof "Hi");
    console.log(typeof typeof true);
    ```

   **Answer**
   - Output1 = string
   - Output2 = string
   - Output3 = string

12. Predict the output:
    ```js
    let a = 10;
    let b = "10";
    console.log(typeof a === typeof b);
    console.log(typeof a == typeof b);
    ```

   **Answer**
   - Output1 = false
   - Output2 = false

13. Predict the output:
    ```js
    console.log(typeof null === "object");
    console.log(typeof [] === "object");
    console.log(typeof {} === "object");
    ```

   **Answer**
   - Output1 = true
   - Output2 = true
   - Output3 = true

14. Predict the output:
    ```js
    let x;
    console.log(typeof x);
    x = null;
    console.log(typeof x);
    x = 0;
    console.log(typeof x);
    ```

   **Answer**
   - Output1 = undefined
   - Output2 = object
   - Output3 = number

15. Predict the output:
    ```js
    console.log(typeof NaN === "number");
    console.log(typeof Infinity === "number");
    console.log(typeof (1 / 0));
    ```

   **Answer**
   - Output1 = true
   - Output2 = true
   - Output3 = number

---

## Part H]: Type Coercion

### Part a:

1. Convert the string `"25"` into a number using `Number()` and add `10` to it. Print the result.  

**Answer**
```js
let string = "25"
string = Number(string)
string += 10
console.log(string)
```

2. Convert the number `100` into a string using `String()` and join it with `" rupees"`. Print the result.  

**Answer**
```js
let number = 100
number = String(number)
number += " rupees"
console.log(number)
```

3. Convert the value `0` into a boolean using `Boolean()` and print it.  

**Answer**
```js
let value = 0
value = Boolean(value)
console.log(value)
```

4. Convert the value `"Hello"` into a boolean and print it.  

**Answer**
```js
let value = "Hello"
value = Boolean(value)
console.log(value)
```

5. Use the unary `+` operator to convert `"50"` into a number and multiply it by `2`.

**Answer**
```js
let value = +"50"*2
console.log(value)
```


### Part b:

6. Predict the output:
   ```js
   console.log("10" - 5);
   console.log("10" + 5);
   console.log("10" * 2);
   console.log("10" / 2);
   ```

   **Answer**
   - Output1 = 5
   - Output2 = 105
   - Output3 = 20
   - Output4 = 5

7. Predict the output:
   ```js
   console.log("5" - "2");
   console.log("5" + "2");
   console.log("5" * "2");
   console.log("5" / "2");
   ```

   **Answer**
   - Output1 = 3
   - Output2 = 52
   - Output3 = 10
   - Output4 = 2.5

8. Predict the output:
   ```js
   console.log(Number("123"));
   console.log(Number("123abc"));
   console.log(Number(true));
   console.log(Number(false));
   console.log(Number(null));
   console.log(Number(undefined));
   ```

   **Answer**
   - Output1 = 123
   - Output2 = NaN
   - Output3 = 1
   - Output4 = 0
   - Output5 = 0
   - Output6 = NaN

9. Predict the output:
   ```js
   console.log(Boolean(0));
   console.log(Boolean(""));
   console.log(Boolean("0"));
   console.log(Boolean([]));
   console.log(Boolean({}));
   console.log(Boolean(null));
   ```

   **Answer**
   - Output1 = false
   - Output2 = false
   - Output3 = true
   - Output4 = true
   - Output5 = true
   - Output6 = false

10. Predict the output:
    ```js
    console.log(String(100));
    console.log(String(true));
    console.log(String(null));
    console.log(String(undefined));
    console.log(100 + "");
    ```

   **Answer**
   - Output1 = 100
   - Output2 = true
   - Output3 = null
   - Output4 = undefined
   - Output5 = 100 

### Part c:

11. Predict the output:
    ```js
    console.log("5" + 3 + 2);
    console.log(5 + 3 + "2");
    console.log("5" - 3 + 2);
    console.log(5 - "3" + "2");
    ```

   **Answer**
   - Output1 = 532
   - Output2 = 82
   - Output3 = 4
   - Output4 = 22

12. Predict the output:
    ```js
    console.log(true + true);
    console.log(true + false);
    console.log(true + "false");
    console.log(false + "true");
    ```

   **Answer**
   - Output1 = 2
   - Output2 = 1
   - Output3 = truefalse
   - Output4 = falsetrue

13. Predict the output:
    ```js
    console.log(null + 5);
    console.log(undefined + 5);
    console.log(null + "5");
    console.log(undefined + "5");
    ```

   **Answer**
   - Output1 = 5
   - Output2 = NaN
   - Output3 = null5
   - Output4 = undefined5

14. Predict the output:
    ```js
    console.log([] + []);
    console.log([] + {});
    console.log({} + []);
    console.log({} + {});
    ```

   **Answer**
   - Output1 = 
   - Output2 = [object object]
   - Output3 = [object Object]
   - Output4 = [object Object][object Object]

15. Predict the output:
    ```js
    let a = "10";
    let b = 5;
    let c = a + b;
    let d = a - b;
    let e = +a + b;
    console.log(c, typeof c);
    console.log(d, typeof d);
    console.log(e, typeof e);
    ```

   **Answer**
   - Output1 = 105 string
   - Output2 = 5 number
   - Output3 = 15 number

16. Predict the output:
    ```js
    console.log(!!"Hello");
    console.log(!!"");
    console.log(!!0);
    console.log(!!1);
    console.log(!!null);
    console.log(!!undefined);
    ```

   **Answer**
   - Output1 = true
   - Output2 = false
   - Output3 = false
   - Output4 = true
   - Output5 = false
   - Output6 = false

17. Predict the output:
    ```js
    console.log(Number(""));
    console.log(Number(" "));
    console.log(Number("0"));
    console.log(Number("  25  "));
    console.log(Number("25px"));
    ```

   **Answer**
   - Output1 = 0
   - Output2 = 0
   - Output3 = 0
   - Output4 = 25
   - Output5 = NaN

18. Predict the output:
    ```js
    let val1 = "5";
    let val2 = 2;
    console.log(val1 + val2);
    console.log(+val1 + val2);
    console.log(val1 - val2);
    console.log(val1 * val2);
    console.log(val1 / val2);
    ```

   **Answer**
   - Output1 = 52
   - Output2 = 7
   - Output3 = 3
   - Output4 = 10
   - Output5 = 2.5

---

# Bonus Mixed Practice Questions:

19. Predict the output:
    ```js
    let count = 5;
    console.log(typeof count++);
    console.log(count);
    console.log(typeof ++count);
    console.log(count);
    ```

   **Answer**
   - Output1 = number
   - Output2 = 6
   - Output3 = number
   - Output4 = 7

20. Predict the output:
    ```js
    let x = "10";
    let y = ++x;
    console.log(x, y, typeof x, typeof y);
    ```

   **Answer**
   - Output = 11 11 number number

21. Predict the output:
    ```js
    let a = "5";
    let b = a++;
    console.log(a, b, typeof a, typeof b);
    ```

   **Answer**
   - Output = 6 5 number number

22. Predict the output:
    ```js
    console.log(typeof (1 + "2"));
    console.log(typeof (1 - "2"));
    console.log(typeof (1 * "2"));
    console.log(typeof (1 / "2"));
    ```

   **Answer**
   - Output1 = string
   - Output2 = number
   - Output3 = number
   - Output4 = number

23. Predict the output:
    ```js
    let val = null;
    console.log(typeof val);
    console.log(val + 1);
    console.log(val - 1);
    console.log(val * 1);
    console.log(Boolean(val));
    ```

   **Answer**
   - Output1 = object
   - Output2 = 1
   - Output3 = -1
   - Output4 = 0
   - Output5 = false

---

**Remember**  
- Focus on understanding **when** and **why** JavaScript converts types automatically.  
- Pay special attention to the difference between `+` (concatenation) and other arithmetic operators.  
- Remember: `typeof null` is a famous historical quirk.  
- Practice predicting outputs before running the code — this builds strong intuition.
