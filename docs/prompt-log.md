# Prompting History & AI Collaboration Log

## Feature 1: Dynamic Overdue Evaluation

### Prompts Used
1. **Prompt 1:** "How do I dynamically check if a task's due date is past the current date in JavaScript/TypeScript without saving a status flag in the database?"
2. **Prompt 2:** "Write a helper function `isTaskOverdue(dueDate: string | Date | null): boolean` that handles null dates safely and returns true only if the date is strictly in the past."
3. **Prompt 3:** "Generate unit test cases for this overdue function covering past dates, future dates, null values, and edge cases like today's date."

---

## Feature 2: Array-Based Tagging System

### Prompts Used
1. **Prompt 4:** "Show me how to model a tags field as an array of strings in a task schema and handle adding unique tags."
2. **Prompt 5:** "Create a React UI component / helper function that renders a list of tags as badges with a button to remove a tag by index or string value."
3. **Prompt 6:** "Write a validation function to sanitize tag input (strip whitespace, enforce lowercase, remove duplicates)."

---

## Prompt Refactoring Example

### Original (Weak) Prompt
> "Fix the tags and make the overdue tasks work properly."

* **Why it was weak:** It lacked technical context, didn't specify input/output types, left room for AI to hallucinate unnecessary complex architecture (like cron jobs or junction tables), and gave no criteria for handling edge cases.

### Refactored (Structured) Prompt
> "Write a TypeScript utility function `calculateOverdueStatus(dueDate: Date | null): boolean`. 
> - If `dueDate` is `null` or `undefined`, return `false`.
> - Compare `dueDate` against `Date.now()`.
> - Return `true` if `dueDate` is strictly less than the current timestamp, otherwise `false`.
> - Include 3 simple Jest unit tests covering: past date, future date, and `null` input."

### Evaluation of AI Output
* **Accepted:** The core boolean logic, date validation checks, and Jest test suite structure.
* **Edited:** Standardized the function name to match our existing helper conventions and imported native Date utilities instead of adding external dependencies.
* **Rejected:** The AI's initial attempt to import `moment.js` for date comparison; replaced it with clean native JS comparisons.