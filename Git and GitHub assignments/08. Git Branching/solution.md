# Git Branching: Hands-on Practice — Create, Switch, Commit & Push Assignments

---

### Assignment 1: Understanding Concepts

*Objective:* Check basic understanding of branching.

*Tasks:*
1. What is a *branch* in Git? Explain in your own words.
2. Why should we *not* work directly on the main branch?
3. Explain the road analogy of branching (main road vs side road).
4. What is the difference between git branch and git switch?

*Submission:* Written answers in your notebook.

**Answers**

<img width="3060" height="3452" alt="20260923_182058" src="https://github.com/user-attachments/assets/72795878-4d7d-4a15-8672-ff6154e65ee0" />

---

### Assignment 2: Commands Identification

*Objective:* Identify the correct commands.

*Tasks:*
1. Write the command for the following actions:

| Action                              | Command |
|-------------------------------------|---------|
| List all branches                   |         |
| Create a new branch named feature-home |    |
| Switch to feature-home            |         |
| Create + Switch in one command      |         |
| Merge feature-home into main      |         |
| Delete feature-home after merge   |         |

2. Write both the *modern* and *older* command for:
   - Switching to a branch
   - Creating + switching to a new branch

*Submission:* Filled table + answers

**Answers**

<img width="3060" height="2608" alt="20260923_182144" src="https://github.com/user-attachments/assets/bcc21ba9-09c5-4aa2-b7c2-1d4f9dd2d19d" />

---

### Assignment 3: Practical Branching Workflow

*Objective:* Perform the complete branching cycle.

*Tasks:*
1. Make sure you are on the main branch.
2. Create a new branch named feature-contact.
3. Create a file contact.txt and write your name + any message.
4. Stage and commit the file with a meaningful message.
5. Switch back to main.
6. Merge feature-contact into main.
7. Delete the feature-contact branch.
8. Verify using:
   - git branch
   - git log --oneline

*Submission:*  
- Screenshot of git branch (before and after)  
- Screenshot of git log --oneline  
- Screenshot showing contact.txt is present on main

**Answers**

<img width="785" height="226" alt="Screenshot 2026-09-23 184159" src="https://github.com/user-attachments/assets/203390a5-f4f6-49e1-9b7d-89dcaee93272" />

<img width="764" height="89" alt="Screenshot 2026-09-23 184040" src="https://github.com/user-attachments/assets/b86bcdb3-33cc-48cc-9c6e-373d93204348" />

<img width="951" height="278" alt="Screenshot 2026-09-23 184300" src="https://github.com/user-attachments/assets/3740f24a-5d7a-49fb-87dc-d9a40a770bc7" />

---

### Assignment 4: Conceptual + Error Handling

*Objective:* Understand rules and common mistakes.

*Tasks:*
1. What will happen if you try to delete a branch that is not yet merged?  
   Write the error and how to fix it.
2. Why should you always *commit* before switching branches?
3. Fill in the correct flow:


______ → Work → ______ → ______ → Switch to main → ______ → Delete branch


4. Explain the difference between:
   - git branch -d branch-name
   - git branch -D branch-name

*Submission:* Written answers

**Answers**

<img width="4080" height="1917" alt="20260923_182235" src="https://github.com/user-attachments/assets/fb9e2e73-cbe6-457f-be7b-8f8034f652d9" />

<img width="3991" height="1442" alt="20260923_182314" src="https://github.com/user-attachments/assets/d437787b-daa1-426f-9541-5ccc0f68ec3a" />

---

### Assignment 5: Complete Real Scenario

*Objective:* Apply branching in a realistic situation.

*Scenario:*  
You are working on a website project. Currently you are on the main branch. You need to add two new pages: *About* and *Services*.

*Tasks:*
1. Create a branch feature-about, add a file about.txt, commit it, merge it into main, and delete the branch.
2. Create another branch feature-services, add a file services.txt, commit it, merge it into main, and delete the branch.
3. After completing both, show:
   - Final list of branches (git branch)
   - Final commit history (git log --oneline)
4. Answer:
   - Why did we create two separate branches instead of doing both features on one branch?
   - What is the advantage of merging only after the feature is complete?

*Submission:*  
- Screenshots of both merges  
- Final git branch and git log --oneline  
- Written answers for the two questions

**Answers**

<img width="772" height="139" alt="Screenshot 2026-09-23 185043" src="https://github.com/user-attachments/assets/d9869307-2326-4da1-b31b-d5a32a78391b" />

<img width="725" height="138" alt="Screenshot 2026-09-23 185415" src="https://github.com/user-attachments/assets/0390ba59-b6b8-4a9c-abb7-568c929a7647" />

<img width="748" height="62" alt="Screenshot 2026-09-23 185503" src="https://github.com/user-attachments/assets/6dd3f081-a1bc-49ae-948c-5d8d53fcacc3" />

<img width="730" height="106" alt="Screenshot 2026-09-23 185525" src="https://github.com/user-attachments/assets/17fef137-6d6c-4326-bfac-f45e3a2a0212" />

<img width="935" height="262" alt="Screenshot 2026-09-23 185717" src="https://github.com/user-attachments/assets/635a9fb5-6b89-4551-bf24-ec2985c8dd5a" />

<img width="3856" height="1421" alt="20260923_182725" src="https://github.com/user-attachments/assets/ebe44d43-c18c-4464-87d7-aaebb4ac4d01" />

---
