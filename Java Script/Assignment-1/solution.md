# Assignment: Introduction to JavaScript
---

## Section A: Short Answer Questions (1 Mark each)

**Q1.** What is JavaScript?

**Answer=** JavaScript is a high-level, dynamically typed programming language used to create interactive websites and applications.

**Q2.** Who created JavaScript and in which year?

**Answer=** JavaScript was created by Brendan Eich in year 1995.

**Q3.** What was the original name of JavaScript?

**Answer=** The Originl name of JavaScript is Mocha.

**Q4.** Is JavaScript the same as Java? Give one major difference.

**Answer=** No, There name is same but they are different Programming languages.

Major Difference = JavaScript is Dynamically Typed language while Java is Statically Typed Language.

**Q5.** What does it mean when we say JavaScript is a **high-level** programming language?

**Answer=** It means JavaScript uses simple and human-readable instructions.

**Q6.** Is JavaScript a compiled language or an interpreted language? Explain briefly.

**Answer=** JavaScript is an interpreted language

Explaination = JavaScript code is executed by a JavaScript engine while the program runs.

**Q7.** Name the JavaScript engines used by the following browsers:
- Google Chrome
- Mozilla Firefox
- Apple Safari

**Answer=** 
- Google Chrome = V8
- Mozilla Firefox = SpiderMonkey
- Apple Safari = JavaScriptCore.

**Q8.** What is **Dynamic Typing** in JavaScript?

**Answer=** JavaScript automatically identifies the data type of a value when the program runs.

**Q9.** What is the main difference between a **static** website and a **dynamic** website?

**Answer=** A static website shows mostly fixed content, while a dynamic website can change content based on users or data.

**Q10.** Name the three pillars of Front-end Web Development and write one line about each.

**Answer=** the three pillars of Front-end Web Development are:-
- Html = It makes the structure of a page.
- Css = It add style to the page.
- JavaScript = It decide the behaviour of the page.

**Q11.** What is the difference between Frontend and Backend?

**Answer=** Frontend is what the user sees and uses. Backend works behind the scenes with servers, databases, and application logic.

**Q12.** What is Node.js?

**Answer=** Node.js is a runtime environment for JavaScript that allows JavaScript to run outside the browser.

**Q13.** Explain **ECMAScript**. What is its relation with JavaScript?

**Answer=** It is a standard or rulebook that defines how the JavaScript language should work.
- Relation = JavaScript is a programming language that follows the ECMAScript standard. JavaScript engines use this standard to understand and execute JavaScript code.

---

## Section B: True or False  
(Write True or False. If False, correct the statement)

1. JavaScript is a statically typed language.

**Answer=** False, JavaScript is a Dynamically typed language.

2. JavaScript can only run inside the browser.

**Answer=** False, JavaScript can run directly in the browser.

3. HTML is responsible for the behaviour of a webpage.

**Answer=** False, JavaScript is responsible for the behaviour of a webpage.

4. Node.js allows JavaScript to run outside the browser.

**Answer=** True

5. JavaScript is case-insensitive.

**Answer=** False, JavaScript is case-sensitive.

6. `let name` and `let Name` are the same variable.

**Answer=** False, `let name` and `let Name` are the different variable.

7. ECMAScript is a programming language.

**Answer=** False, ECMAScript is a standard or rulebook.

8. React, Angular, and Vue.js are used for Backend development.

**Answer=** False, React, Angular, and Vue.js are used for Frontend development.

---

## Section C: Fill in the Blanks

1. JavaScript was created by **Brendan Eich** in the year **1995**.
2. The three technologies used in Front-end development are **HTML**, **CSS**, and **JavaScript**.
3. JavaScript engines: Chrome uses **V8**, Firefox uses **SpiderMonkey**.
4. In the restaurant analogy: Customer = **Frontend**, Waiter = **API**, Chef = **Backend**.
5. JavaScript file extension is **.js**.

---

## Section D: Conceptual Questions (2 Marks each)

**Q14.** Differentiate between a **static website** and a **dynamic website**. Give one real-world example of each.

**Answer=**

A Static website can only show Fixed content, links and images. Nothing changes after the page load.
- Example=A simple personal portfolio website.

A dynamic website generates or updates content based on data or user interaction.
- Example=Amazone, youtube etc..

**Q15.** Explain any two features of JavaScript that make it suitable for creating interactive web pages.

**Answer=**
- Event-Driven=JavaScript can respond to events caused by the user or browser.

Example= Click, Keydown, load, submit.
- Dynamic Typing=JavaScript automatically identifies the data type of a value when the program runs.

**Q16.** List any four areas (apart from web browsers) where JavaScript is used today. Mention one popular framework/library for each (if applicable).

**Answers**
- Mobile App Development-React Native
- Game Development-Phaser
- Server-Side Development-Node.js
- Desktop Application Development-Electron

**Q17.** What is the difference between writing JavaScript code:
- Inside an HTML file using `<script>` tag, and
- In an external `.js` file?  
Mention two advantages of using an external JavaScript file.

**Answer=**
- Inside an HTML file using `<script>` tag = JavaScript code is written directly inside the HTML file. Which is suitable for small script or simple webpages.
- In an external `.js` file = JavaScript code is written in a separate '.js' file. Which is Suitable for larger projects and multiple webpages.

**Two Advantages of External JavaScript**
- JavaScript is kept separate from HTML, making the code easier to read, manage, and update.
- The same '.js' file can be linked to multiple HTML pages.

**Q18.** Explain the difference between Frontend and Backend using the **restaurant analogy** in your own words.

**Answer=** A user is like customer who sits at the table and places an order. Frontend is like a dining area, menu, tables and waiter which a customer can see and interact. Backend is like kitchen and chef which make the ordered food for customer.

**Q19.** Why should a beginner learn JavaScript? Write at least 4 points.

**Answer=**
- JavaScript is relatively simple for beginners to learn.
- It helps beginners build complete and interactive websites.
- It can be used for web development, mobile apps, games, and server-side programming.
- It adds features like buttons, animations, forms, and menus.

---

## Section E: Code-Based Questions (3 Marks each)

**Q20.** Predict the output of the following code and explain why:

```javascript
let value = 25;
console.log(typeof value);
value = "JavaScript";
console.log(typeof value);
value = false;
console.log(typeof value);

**Answer=**1.integer, 2.string, 3.boolean.

Explaination=The first consol will show the type of data stored in variable value which is integer. The second console will show the type of new data stored in value variable which is string. the third console will show the type of new data stored in value variable which is a boolean.

```

**Q21.** Write a simple HTML + JavaScript program that displays an alert box with the message **"Welcome to JavaScript!"** when a button is clicked.

**Answer=**

![alt text](<Screenshot 2026-09-28 184938.png>)

**Q22.** Write JavaScript code to demonstrate **event-driven programming**.  
When a user clicks a button with id `"myBtn"`, the text of a paragraph with id `"demo"` should change to `"Button was clicked!"`.

**Answer=**
![alt text](<Screenshot 2026-09-28 184857.png>)

---

## Section F: Practical / Application Based (5 Marks)

**Q23.** Create a complete web page (HTML + JavaScript) that includes the following:

1. A heading: **"My First JavaScript Page"**
2. A button labeled **"Click Me"**
3. When the button is clicked:
   - Show an alert: `"Hello, B.Tech Student!"`
   - Change the background color of the page to light blue
4. Also print `"JavaScript is running successfully!"` in the browser console.

**Write the complete code** (you can use Inline or External JavaScript).

**Answer=**

![alt text](<Screenshot 2026-09-28 184907.png>)

---

## Section G: Higher Order Thinking (Bonus - 3 Marks)

**Q24.** JavaScript was originally created only for browsers. Today it is used in frontend, backend, mobile apps, desktop apps, and even AI/ML.  
In your own words, explain why JavaScript became so popular and multipurpose. Mention the role of **Node.js** and **ECMAScript** updates in this growth.

**Answer=** JavaScript became popular because it is easy to use and works across many platforms. It can be used for websites, servers, mobile apps, and desktop apps. Node.js allowed JavaScript to run outside browsers. ECMAScript updates added new features and improved JavaScript over time. Its large ecosystem also helped it grow.
---

### Submission Guidelines
- Write your answers in a notebook or type them in a document.
- For coding questions, test your code using browser console, VS Code Live Server, or online editors (CodePen / JSFiddle).
- Submit the answers on Github CodingGita Assignment Repo in JavaScript Folder before the given deadline.

**All the Best!**

---