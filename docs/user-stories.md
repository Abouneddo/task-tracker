# User Stories & AI Assumption Log

## Feature 1: Dynamic Overdue Status Evaluation

### User Stories
1. **As a** user, **I want** tasks past their due date to automatically highlight as "Overdue", **so that** I can prioritize urgent work immediately.
   * **Acceptance Criteria:**
     * Given a task with a due date in the past, when viewed, the UI displays an "Overdue" status tag in red.
     * Given a task with a due date in the future, when viewed, the status remains normal.
2. **As a** user, **I want** tasks without a due date to never mark as overdue, **so that** unscheduled tasks aren't flagged incorrectly.
   * **Acceptance Criteria:**
     * Given a task with no due date (`null`), the overdue check returns `false`.
3. **As a** user, **I want** overdue statuses to update live when I open the app without needing manual refreshes, **so that** I always see accurate state.
   * **Acceptance Criteria:**
     * Status is calculated dynamically using current time on render/fetch.

### AI Assumption Corrected
* **AI Assumption:** The AI initially assumed we needed a background job (cron job) running on a server to update an `is_overdue` boolean field in the database every midnight.
* **Correction:** I corrected the AI to evaluate `isOverdue` dynamically on the client/read-getter using the current system time (`dueDate < Date.now()`). This avoided unnecessary database write operations and background worker complexity.

---

## Feature 2: Array-Based Tagging System

### User Stories
1. **As a** user, **I want** to attach multiple tags (e.g., "Work", "Urgent") to a task, **so that** I can organize my tasks efficiently.
   * **Acceptance Criteria:**
     * User can type a tag name and hit Enter to add it to a list on the task.
2. **As a** user, **I want** to remove an existing tag from a task, **so that** I can update categorization when plans change.
   * **Acceptance Criteria:**
     * Clicking the "X" button next to a tag badge removes it from the task's tag array.
3. **As a** user, **I want** duplicate tags to be automatically ignored on the same task, **so that** my task view stays clean.
   * **Acceptance Criteria:**
     * Adding a tag that already exists in the array does not create a second duplicate badge.

### AI Assumption Corrected
* **AI Assumption:** The AI assumed a complex normalized SQL database setup with a `Tags` table and a `Task_Tags` junction table (many-to-many relationship).
* **Correction:** I directed the AI to use simple native array storage (e.g., `tags TEXT[]` or a JSON array field) to keep the data schema lightweight and fast for this project's scope.