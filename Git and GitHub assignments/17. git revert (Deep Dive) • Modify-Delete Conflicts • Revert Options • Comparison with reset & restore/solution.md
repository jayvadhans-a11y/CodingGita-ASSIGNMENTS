# Assignment - git revert • Modify/Delete Conflict • Revert Options • Comparison with reset & restore

---

## Instructions

- Use your **CodingGita_Assignment** repository for all practical work and submission.
- Complete the assignments in order.
- For theoretical questions → write a short and correct answer in your notebook.
- Take clear photos of the written answers.
- Take screenshots of terminal / GitHub where asked.
- Push your practical work to the repository and submit the repository link along with the required photos and screenshots.

**Before you start:** Make sure your working directory is clean (`git status`).

---

## Assignment 1 – Basic Revert Practice

**Goal:** Perform a simple revert and observe the new commit.

1. Create 2–3 commits on any file (for example `index.html` or `notes.txt`).
2. Using `git log --oneline`, note the commit hash of the latest commit.
3. Revert the latest commit:
   ```bash
   git revert HEAD
   ```
   (or use the commit hash)
4. Run `git log --oneline` and observe the new revert commit.

**Submit:**
- Screenshot of `git log --oneline` before revert
- Screenshot of `git log --oneline` after revert
- Repository link

**Answers**
GitHub Repo Link = https://github.com/jayvadhans-a11y/Basic-Revert-Practice.git

<img width="706" height="118" alt="day 17 s1" src="https://github.com/user-attachments/assets/fcfd63eb-a821-4ff0-b1c8-c50229d16e8b" />

<img width="721" height="135" alt="day 17 s2" src="https://github.com/user-attachments/assets/758dff9c-88c3-4c6a-974f-9f2739d81cbd" />

---

## Assignment 2 – Modify/Delete Conflict during Revert

**Goal:** Face and resolve a Modify/Delete conflict while reverting.

1. Create a commit that **adds a new file**.
2. Make one more commit after that.
3. Try to revert the commit that added the file.
4. A Modify/Delete conflict should appear.
5. Resolve it (either delete the file or keep it with required content).
6. Use:
   ```bash
   git add .
   git revert --continue
   ```

**Submit:**
- Screenshot of the conflict (VS Code or terminal)
- Screenshot after successful `git revert --continue`
- Repository link

**Answers**
GitHub Repo Link = https://github.com/jayvadhans-a11y/Modify-Delete-Conflict-during-Revert.git

<img width="1138" height="206" alt="day 17 s3" src="https://github.com/user-attachments/assets/db4ef00e-567e-4f60-96d4-cda50a6af1f4" />

<img width="922" height="225" alt="day 17 s4" src="https://github.com/user-attachments/assets/7ce78ecc-61ed-4d81-bf1a-19ca3af7542a" />

---

## Assignment 3 – Revert Options + Conceptual Questions

**Goal:** Practice important flags and understand the concepts.

### Practical Part
1. Demonstrate any two of the following commands with a real commit:
   - `git revert --no-edit <commit_id>`
   - `git revert --no-commit <commit_id>`
   - `git revert --abort`
2. Take screenshots of the commands and their results.

### Theoretical Part (Write in Notebook)
Write short and correct answers for the following:

1. What does `git revert` do?
2. Why is `git revert` safer than `git reset` on a shared branch?
3. What is a Modify/Delete conflict? When can it occur during revert?
4. What is the difference between `git revert --abort` and `git revert --quit`?
5. Write one major difference each between:
   - `git restore`
   - `git reset`
   - `git revert`

**Submit:**
- Screenshots of the two practical commands you tried
- Clear photos of the written answers from your notebook
- Repository link

---

## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – before & after log screenshots | Yes |
| 2 | Assignment 2 – conflict + resolution screenshots | Yes |
| 3 | Assignment 3 – practical screenshots + notebook photos | Yes |
| — | CodingGita_Assignment repository link | Yes |

**Important:**
- Push all practical work to your **CodingGita_Assignment** repository.
- Theoretical answers must be handwritten in notebook (photos required).
- Make sure screenshots and photos are clear and readable.

**Answers**
GitHub Repo Link = https://github.com/jayvadhans-a11y/Revert-practical-part.git

<img width="1135" height="466" alt="day 17 s5" src="https://github.com/user-attachments/assets/719b54bf-d323-465c-9ce5-9a6e08cef7db" />

<img width="734" height="390" alt="day 17 s6" src="https://github.com/user-attachments/assets/48c192bd-4c4f-4aae-bdbf-677e3f720450" />

<img width="2614" height="3126" alt="20260921_175317" src="https://github.com/user-attachments/assets/f1fe2552-d62b-407b-989b-562f44e6cbd2" />

<img width="3191" height="836" alt="20260921_175359" src="https://github.com/user-attachments/assets/aef6fef7-f1dd-4a0d-8d94-6c721aea56ea" />

---

# Deadline: 5th Sepetember, 2026.
