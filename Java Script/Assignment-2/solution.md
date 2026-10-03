# Assignment : Introduction to Variables and Datatypes
---
## Part I : Variables (let, var, const)

### Part a — 4 Questions

**1. Personal Information**
Declare variables for `name`, `age`, and `city` using appropriate variable keywords. Assign values and print all three variables.

**Answer**
```javascript
let name="Anil";
let age=16;
let city="Udaipur";
console.log(name);
console.log(age);
console.log(city)
```

**2. Change the Score**
Create a variable `score` with the value `50`. Change its value to `80` and print the final value. Use the appropriate keyword for a value that can change.

**Answer**
```javascript
let score=50;
score=80;
console.log(score)
```

**3. Constant Value**
Create a constant variable `PI` with the value `3.14`. Print its value. Do not try to change the value.

**Answer**
```javascript
const PI=3.14;
console.log(PI)
```

**4. Uninitialized Variables**
Declare one variable having name `num1` using `var` and one having name `num2` using `let` without assigning values. Print both variables. Then assign values to them and print the values again.

**Answer**
```javascript
var num1
let num2
console.log(num1)
console.log(num2)

num1=15
num2=17
console.log(num1)
console.log(num2)
```

---

### Part b — 4 Questions

**5. Choose the Correct Keyword**
Create the following variables using the most appropriate keyword:

* `studentName` — the value will not change
* `marks` — the value may change
* `schoolName` — the value will not change

Assign values to all three variables. Change `marks` and print all variables.

**Answer**
```javascript
const studentName="Anil"
let marks=67
const schoolName="Ascent"
marks=89
console.log(studentName)
console.log(marks)
console.log(schoolName)
```

**6. Understand Scope**
Write a program where `var`, `let`, and `const` variables are declared inside an `if` block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.

**Answer**
```javascript
if (true){
    var a = 10;
    let b = 20;
    const c = 30;
    console.log(a);
    console.log(b);
    console.log(c);
}
console.log(a);
console.log(b);
console.log(c);
```

Explaination=only var variable can access outside the block.

**7. Test Re-declaration**
Declare a variable named `user` using `var` and declare it again with a different value. Then perform the same experiment using `let`. Observe what happens and identify which declaration allows re-declaration.

**Answer**
```javascript
var user="Anil"
var user="Omprakash"
console.log(user)

let user="Vedant"
let user="Sankalp"
console.log(user)
```

Explaination: only var declaration allow re-declaration.

**8. Test Re-assignment**
Create three variables using `var`, `let`, and `const`. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.

**Answer**
```javascript
var a="Anil"
let b=16
const c="Rahul"
a="Hari"
b=18
c="Ramu"
console.log(a)
console.log(b)
console.log(c)
```

Explaination=only var and let variable allow re-assignment and const produces an error.

---

### Part c — 2 Questions

**9. Predict and Explain**
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

```javascript
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y);
console.log(z);
```

**Answer**
Explaination="console.log(x)" will give 20 as output and Other 2 console will give the error

**10. Fix the Program**
The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for **initialization, re-declaration, re-assignment, and scope**.

```javascript
const name;

let age = 20;
let age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
}

console.log(country);

const score = 50;
score = 80;
```

**Answer**
```javascript
const name="Rahul"
console.log(name)

var age = 20;
var age = 25;
console.log(age)

if (true) {
    var city = "Delhi";
    var country = "India";
}

console.log(country);

let score = 50;
score = 80;
console.log(score)
```

#### Part d — 2 Question 

**11. Predict the Hoisting Behavior**  
Without running the code, predict the output of each `console.log()` and identify which lines cause errors. Explain your answer using the rules of hoisting for `var`, `let`, and `const`.

```javascript
console.log(a);
console.log(b);
console.log(c);

var a = 10;
let b = 20;
const c = 30;
```

**Answer**
explaination="console.log(a)" will give undefined and "console.log(b) and console.log(c)" will give error because as b & c is let and const 
we need to initialize them before print it.

**12. Fix the Hoisting Errors**  
The following program contains errors related to hoisting. Fix the code so that it runs correctly without any errors. Make sure your solution follows the rules of hoisting for `var`, `let`, and `const` (you may reorder declarations/assignments or change keywords only where necessary to make it work properly).

```javascript
console.log(x);
console.log(y);
console.log(z);

var x = "Hello";
let y = "World";
const z = "!";

console.log(x + " " + y + z);
```

**Answer**
```javascript
var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z);
```

**Questions on Primitive vs Non-Primitive Data Types**

---

### Part e — Basic Identification (4 Questions)

**1. Classify the Types**  
Declare one variable of each of the following types and print both the value and its type using `typeof`:
- A whole number  
- A decimal number  
- A piece of text  
- A true/false value 

**Answer**
```Javascript
let a= 5
let b= 5.6
let c= "Hello"
let d= false
console.log(a, typeof(a))
console.log(b, typeof(b))
console.log(c, typeof(c))
console.log(d, typeof(d))
```

**2. Undefined vs Null**  
Declare two variables:
- `a` using `let` without assigning any value  
- `b` and intentionally assign `null` to it  

Print both variables and their `typeof` results. Explain the difference between `undefined` and `null`.

**Answer**
```Javascript
let a;
let b= null
console.log(a, typeof(a))
console.log(b, typeof(b))
```
Explaination =- undefined value occure when we declare a variable but not assigned any value to it.
- Null value do not occure automatically. It ocure when we assign it to a variable which we want to be empty. It represent no value

**3. Number Special Values**  
Create variables for the following and print each value along with its type:
- Positive Infinity  
- Negative Infinity  
- Not-a-Number (`NaN`)  
- A large number written with scientific notation (e.g., `2.5e3`)  
- A number written with underscores for readability (e.g., `1_000_000`)

**Answer**
```Javascript
let a= Infinity
let b= -Infinity
let c= NaN
let d= 2.5e3
let e= 1_000_000
console.log(a, typeof(a))
console.log(b, typeof(b))
console.log(c, typeof(c))
console.log(d, typeof(d))
console.log(e, typeof(e))
```

**4. String Styles**  
Create three string variables using:
- Single quotes  
- Double quotes  
- Template literals (backticks) that include another variable  

Print all three strings.

**Answer**
```Javascript
var name='Jayvardhan singh'
let subject="JavaScript"
const city=`ahamdabad`
console.log(name)
console.log(subject)
console.log(city)
```

---

### Part f — Advanced Primitive Types (3 Questions)

**5. Symbol Uniqueness**  
Create two Symbols with the same description (`'id'`).  
Compare them using `===` and print the result.  
Then use both Symbols as keys in an object and retrieve the values.  
Explain why the comparison returns `false`.

**Answer**
```javascript
let a=Symbol('id')
let b=Symbol('id')
console.log(a===b)

let c = {
  [a]: 1,
  [b]: 2
};
console.log(c[a]);
console.log(c[b]);
```
explaination=the comparison of a and b return false because every symbol create a unique value. Even if it's look same both are different.

**6. BigInt Precision**  
Create a regular `number` with the value `9007199254740991` (Number.MAX_SAFE_INTEGER).  
Add `1`, `2`, and `3` to it and print the results.  
Now create the same value as a `BigInt` and perform the same additions.  
Print the results and explain the difference.

**Answer**
```javascript
let num=9007199254740991
console.log(num + 1);
console.log(num + 2);
console.log(num + 3);

let num2=9007199254740991n
console.log(num2 + 1n);
console.log(num2 + 2n);
console.log(num2 + 3n);
```
explaination= the bigint values give the correct answer of addition while number value lost the precicion at such big values.

**7. Choose the Correct Type**  
For each description below, write the most appropriate primitive data type and give an example declaration:
- A unique identifier that is never equal to another value with the same description  
- A very large integer that must keep exact precision  
- A variable that has been declared but not yet given a value  
- An intentional empty value  

**Answer**
- primitive Type= Symbol ,Example= let a= let a=Symbol("key")
- primitive Type= bigint ,Example= let b= 1234567890n
- primitive Type= undefined ,Example= let c;
- primitive Type= null ,Example= let d=null;
---

### Part g — Prediction & Fixing (3 Questions)

**8. Predict the Output**  
Without running the code, predict what each `console.log` will print (value + type). Explain your reasoning.

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);
console.log(typeof b, b);
console.log(typeof c, c);
console.log(typeof d, d);
console.log(typeof e, e);
console.log(typeof f, f);
console.log(typeof g, g);
```
**Answer**
Explaination=- "console.log(typeof a, a)" will print "undefined undefined" because 'a' do not have any value so javascript will automatically assign it a value 'undefined' and it's type is also 'undefined'. 
- "console.log(typeof b, b)" will print "object null" because we already assign it a value 'null' which means 'no value' and it's type is Object.
- "console.log(typeof c, c)" will print "number 42" 42 is number so its type is also a number.
- "console.log(typeof d, d)" will print "string Hello" Hello type is string because string represent text and hello is also a text.
- "console.log(typeof e, e)" will print "boolean true" as true type is boolean because boolean represents logical values and true is also a logical value.
- "console.log(typeof f, f)" will print "symbol Symbol(key)" because symbol used for special internal purposes.
- "console.log(typeof g, g)" will print "bigint 123n" because bigint represent very large integer which is either large in digits or have n at the end.

**9. Fix the Code**  
The following program has mistakes related to primitive types. Fix it so that it runs correctly and prints meaningful values.

```javascript
let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = "Null";
let unique = symbol("id");
let big = 9007199254740991;

console.log(num, text, flag, empty, nothing, unique, big);
```

**Answer**
```javascript
let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = null;
let unique = Symbol("key");
let big = 9007199254740991;

console.log(num, text, flag, empty, nothing, unique, big);
```

**10. Primitive vs Non-Primitive**  
Answer the following questions in your own words and give one example for each:

a) What is the main difference between Primitive and Non-Primitive data types?  
b) Why are Numbers, Strings, Booleans, Undefined, Null, Symbol, and BigInt called Primitive?  
c) Give one example of a Non-Primitive data type and explain why it is considered Non-Primitive.

**Answer**
- a = Primitive data types are the basic and fundamental data types Whereas Non-Primitive data types are complex data type made from primitive data types.
- b = Because all of them can hold only a single value at a time but non-primitive data type can hold multiple values at a time.
- c = Example = Array, explaination = because array can hold multiple values at a time.
```javascript
let numbers = [1, 2, 3, 4, 5]; // Example of single array= these all are fom number data type.
let mixed = [1, "hello", true, null]; // Example of mixed array= these all are from different data types.
```


---

### Part H] - Non-Primitive Data Types Basic Creation & Usage (4 Questions)

**1. Create an Object**  
Create an object named `student` with the following properties:
- `name` → `"Riya"`
- `age` → `18`
- `isEnrolled` → `true`  

Print the entire object and then print each property individually.

**Answer**
```javascript
let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
}

// print the enite object
console.log(student)

// print each property individually
console.log(student.name)
console.log(student.age)
console.log(student.isEnrolled)
```

**2. Work with Arrays**  
Create two arrays:
- `scores` containing only numbers: `85, 92, 78, 90`
- `mixedData` containing different types: a number, a string, a boolean, and `null`  

Print both arrays. Also print the first and last element of the `scores` array using index.

**Answer**
```javascript
let scores = [85, 92, 78, 90];
let mixedData = [16, "Rahul", true, null];
console.log(scores)
console.log(mixedData)
console.log(scores[0])
console.log(scores[scores.length-1])
```

**3. Declare and Call a Function**  
Write a function named `calculateArea` that takes two parameters (`length` and `width`) and returns the area of a rectangle.  
Call the function twice with different values and print the results.

**Answer**
```javascript
function calculateArea (length, width){
    return(length*width)
}
console.log(calculateArea(10, 7))
console.log(calculateArea(9, 4))
```

**4. Check Types with `typeof`**  
Create variables of the following types and print both the value and its type using `typeof`:
- A number  
- A string  
- A boolean  
- `null`  
- An object  
- An array  
- A function  

Observe and note any surprising results (especially with `null` and arrays).

**Answer**
```javascript
let num = 16
let name = "Rahul"
let isStudent = true
let empty = null
let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
}
let scores = [85, 92, 78, 90];
function calculateArea (length, width){
    return(length*width)
}
console.log(num, typeof(num))
console.log(name, typeof(name))
console.log(isStudent, typeof(isStudent))
console.log(empty, typeof(empty))
console.log(student, typeof(student))
console.log(scores, typeof(scores))
console.log(calculateArea(10, 7), typeof(calculateArea))
```

---

### Part I] - Naming Rules & Best Practices (3 Questions)

**5. Valid vs Invalid Variable Names**  
Identify which of the following variable names are **valid** and which are **invalid**. For invalid ones, explain why.

```javascript
let userName;
let 2ndPlace;
let _privateData;
let $price;
let my-age;
let function;
let totalCount;
let const;
```

**Answer**
- let userName; = Valid variable name.
- let 2ndPlace; = Invalid, because a variable name cannot start with a number.
- let _privateData; = Valid variable name.
- let $price; = Valid variable name.
- let my-age; = Invalid, because hyphen not allowed in variable name.
- let function; = Invalid, because we cannot use reserved keyword for variable name.
- let totalCount; = Valid variable name.
- let const; = Invalid, because we cannot use reserved keyword for variable name.

**6. Apply Best Practices**  
Rewrite the following poorly written code using best practices (`const`/`let`, meaningful names, camelCase, UPPERCASE for constants):

```javascript
let a = 10;
let b = 5;
let c = a * b;
let d= 100;
```

**Answer**
```javascript
const LENGTH = 10;
const WIDTH = 5;
const areaOfRectangle = LENGTH * WIDTH;
const MAX_VALUE= 100;
```

**7. Declaration & Assignment**  
Write code that demonstrates:
- Declaring a variable without assigning a value, then assigning a value later  
- Declaring and assigning a value in one step  
- Creating a constant that cannot be changed  

Print all variables.

**Answer**
```javascript
let num;
num = 17;
let num1 = 10;
const num2 = 5;
console.log(num)
console.log(num1)
console.log(num2)
```
---

### Part J] - Prediction & Fixing (3 Questions)

**8. Predict the Output**  
Without running the code, predict what each `console.log` will print. Explain your reasoning (especially for `typeof`).

```javascript
let person = { name: "Amit", age: 22 };
let colors = ["red", "green", "blue"];
function sayHi() {
  return "Hi!";
}
let empty = null;

console.log(typeof person);
console.log(typeof colors);
console.log(typeof sayHi);
console.log(typeof empty);
console.log(person.name);
console.log(colors[1]);
console.log(sayHi());
```

**Answer**
- console.log(typeof person); = It will print "Object" Because it is an `Object` and an `Object` type is also `Object`.
- console.log(typeof colors); = It will print "Object" Because it is an `array` and an `array` type is `Object`.
- console.log(typeof sayHi); = It will print "function" Because it is an `function` and an `function` type is also `function`.
- console.log(typeof empty); = It will print "Object" Because it is an `null` and an `null` type is also `null` but javascript print it as `Object` because it is an javascript quirk.
- console.log(person.name); = It will print "Amit" Because `person` is an `object` so it will print the value which is stored inside it with `name` key which is `Amit`
- console.log(colors[1]); = It will print "red" Because `color` is an `array` so it will print that value which is stored inside it at `1` place which is `red`.
- console.log(sayHi()); = It will print "Hi!" Because it is a function so it will print the value we tell it to return .

**9. Fix the Program**  
The following code has multiple errors related to objects, arrays, functions, naming rules, and best practices. Fix it so that it runs correctly.

```javascript
let 1student = { name: "Neha", Age: 19 }
let scores = 90, 85, 88
function greet {
  return "Hello " + name
}
const maxScore = 100
maxScore = 95
console.log(1student.name)
console.log(scores[0])
console.log(greet("Neha"))
```

**Answer**
```javascript
let student = { name: "Neha", Age: 19 };
let scores = (90, 85, 88)
function greet(name) {
  return "Hello " + name
}
let maxScore = 100
maxScore = 95
console.log(student.name)
console.log(scores[0])
console.log(greet("Neha"))
```

**10. Concept Questions**  
Answer the following in your own words with examples:

a) What is the main difference between an **Object** and an **Array**?  
b) Why does `typeof null` return `"object"`? Is `null` really an object?  
c) Why is it recommended to keep arrays with a single data type?  
d) When should you use `const` and when should you use `let`?

**Answer**
- a = An object can store any type of data with a specific key for that inside it.But an array is recommended to store only one type of data in it to make it easier for programming language.
- b = No, `null` type is also `null` but `typeof null` return `"object"` because it is a javascript quirk which is made when javasciprt is created.
- c = Arrays are usually recommended to contain a single data type because it makes them easier and more efficient for a programming language to manage.
- d = We can use `const` when we don't want to change the value of a variable later.We can use `let` when we want to change the value of a variable later.