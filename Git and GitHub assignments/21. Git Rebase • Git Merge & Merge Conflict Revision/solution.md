# Assignment: Git Rebase, Git Merge & Merge Conflict

**Instructions:** Attempt all questions. Use proper Git commands and show the required commit history wherever asked.

---

## Q1. Rebase, Merge & Merge Conflict 

Answer the following:

1. Define **Git Merge**, **Merge Conflict**, and **Git Rebase**.
2. Explain **Merge vs Rebase** with a suitable diagram.
3. Write three advantages of Git Rebase.
4. Explain why Rebase is useful in real-life projects.
5. Explain the purpose of:

   * `git rebase --continue`
   * `git rebase --abort`
   * `git rebase --skip`

**Answers :**

<img width="3060" height="4080" alt="20260920_141552" src="https://github.com/user-attachments/assets/bb56bd17-cee7-4583-9a00-dad7ddcd700e" />

<img width="3033" height="2690" alt="20260920_141640" src="https://github.com/user-attachments/assets/266f401c-433d-404d-a8aa-f9e5b88771f5" />

---

## Q2. Merge and Rebase

### Scenario: E-Commerce Website

You are working on an e-commerce project.

Create the following scenario yourself:

* Create a `main` branch.
* Create a branch named `product-page`.
* Make **two commits** on `product-page` related to the product page.
* Make **two new commits** on `main` related to other website updates.

### Tasks

1. Show the commit history using a diagram similar to:

```text
A---B---C---D  main
     \
      E---F    product-page
```

Use your **own meaningful commit messages** instead of `A, B, C...`.

2. Merge `product-page` into `main`.
3. Show the commit history after the merge (submit the screenshot).
4. Reset/recreate the scenario if required and perform a **rebase of `product-page` onto `main`**.
5. Show the commit history after the rebase(submit the screenshot).
6. Write **two differences** you observed between the merge and rebase results.

 
** Submission ** : GitHub Repo link + Screenshots + Photos of written answers

**Answers :**

GitHub Repo Link="https://github.com/jayvadhans-a11y/Git-Merge-and-Rebase.git"

<img width="706" height="117" alt="Screenshot 2026-09-20 115414" src="https://github.com/user-attachments/assets/9e388050-0f6b-44c2-811a-bbcd89894a3b" />

<img width="773" height="122" alt="day 21 s2" src="https://github.com/user-attachments/assets/05f4d00a-dfaf-4093-a11e-c9657c27f71d" />

<img width="695" height="166" alt="day 21 s3" src="https://github.com/user-attachments/assets/9ff8a485-e7e7-4400-a613-3db562f1c9c1" />

<img width="754" height="155" alt="day 21 s4" src="https://github.com/user-attachments/assets/e282af21-af52-4dd0-99fe-0c549680798f" />

<img width="1620" height="3825" alt="20260920_141727" src="https://github.com/user-attachments/assets/f101dc70-fa02-4485-8916-be176b17dada" />

---

# Q3. Rebase Conflict

### Scenario: Student Management System

You are developing a student management system.

Create your own Git scenario using:

* `main` branch
* `student-profile` branch

### Tasks

1. Create the `student-profile` branch from `main`.
2. On `student-profile`, make **two commits** related to the student profile.
3. Switch to `main` and make a change to the **same line of the same file**.
4. Switch back to `student-profile`.
5. Rebase `student-profile` onto `main`:

```bash
git rebase main
```

6. Resolve the rebase conflict.
7. Complete the rebase using:

```bash
git add .
git rebase --continue
```

8. Create another small rebase-conflict scenario and demonstrate:

```bash
git rebase --abort
```

Explain what happened to the branch after aborting.

9. Demonstrate:

```bash
git rebase --skip
```

Explain which commit was skipped.

10. Finally, display the commit history using following command and submit the screenshot:

```bash
git log --oneline --graph --all
```

** Submission ** : GitHub Repo link + Screenshots + Photos of written answers.

**Answers :**

GitHub Repo Link="https://github.com/jayvadhans-a11y/git-rebase-conflict.git"

<img width="3060" height="4080" alt="20260920_141808" src="https://github.com/user-attachments/assets/4f34a22f-1459-4a27-aebe-6bdc1c98af0e" />

<img width="842" height="127" alt="day 21 s5" src="https://github.com/user-attachments/assets/d334dc28-0645-4876-ab2d-8c6a6e69f630" />

---
