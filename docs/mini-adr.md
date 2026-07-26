# Architecture Decision Records (ADRs)

## ADR 1: Dynamic Property Evaluation for Overdue Items

### Status
Accepted

### Context
Tasks require an overdue status to inform users when a deadline has passed. We needed to decide how to calculate and persist this state across the application. 

### Decision
We decided to evaluate the overdue status **dynamically on-the-fly** (using a getter/helper function like `dueDate < Date.now()`) rather than persisting an `is_overdue` boolean flag in the database or using background workers (cron jobs) to periodically update records.

### Consequences
* **Pros:**
  * **Zero Infrastructure Overhead:** Avoids setting up background job queues, scheduled cron tasks, or serverless timers.
  * **Real-time Accuracy:** Prevents stale data. A task is evaluated against the exact current timestamp at the moment it is retrieved or rendered.
  * **Reduced Database Writes:** Eliminates unnecessary database write operations just to update a status flag.
* **Cons:**
  * Requires a minor computational check on each read/render operation, though the performance cost is negligible.

---

## ADR 2: Direct Array Storage for Tags

### Status
Accepted

### Context
Tasks need a flexible way to be categorized using custom labels/tags. We needed to choose between a fully normalized database schema or a simplified array storage approach.

### Decision
We decided to store task tags using **native array storage** (e.g., `tags TEXT[]` or a JSON/string array column within the main Task table) rather than creating separate `Tags` and `Task_Tags` junction tables.

### Consequences
* **Pros:**
  * **Simplified Schema:** Keeps the database model straightforward and avoids multi-table SQL joins (`JOIN`) when fetching tasks.
  * **Faster Read Performance:** Retrieves all task metadata, including tags, in a single query payload.
  * **Reduced Code Boilerplate:** Simplifies CRUD operations, API controllers, and frontend state management.
* **Cons:**
  * Makes global tag management (e.g., renaming a tag across every task in the database) more resource-intensive, which is an acceptable trade-off for the current project scope.