# Final Project Reflection

## AI Tool Integration
Throughout this project, AI assistants (such as ChatGPT/Claude) were integrated alongside standard development tools, including VS Code, Git, and automated testing frameworks. The primary role of the AI was to serve as a pair programmer—speeding up boilerplating, generating unit tests, and assisting in initial feature scaffolding. Meanwhile, core architectural decisions, code reviews, and environment-specific troubleshooting (such as resolving terminal/shell command execution issues) were managed directly.

## Productivity Accelerators
AI tools significantly boosted efficiency across several repetitive tasks:
* **Test Suite Generation:** Instantly drafting test structures for edge cases (e.g., past dates, future dates, `null` parameters) saved substantial time compared to writing assertions manually from scratch.
* **Refactoring Ideas:** Using AI to brainstorm utility implementations provided clear starting points for handling array filtering and string sanitization.
* **Documentation Structuring:** Formatting user stories, acceptance criteria, and architecture decision logs was streamlined by converting rough thoughts into standardized markdown structures quickly.

## Human Oversight & Preventing Over-Engineering
While AI models excel at generating functional code, they frequently default to over-engineered patterns. Active human review proved essential in keeping the project's scope clean and lightweight:
1. **Dynamic Overdue Evaluation:** The AI initially suggested setting up a background worker or cron job to regularly update an `is_overdue` database column. Strict human intervention rejected this unnecessary infrastructure complexity in favor of a clean, dynamic client/getter date check (`dueDate < Date.now()`).
2. **Simplified Schema for Tags:** When tasked with tag management, the AI proposed fully normalized relational models featuring dedicated `Tags` and `Task_Tags` junction tables. Recognizing the overhead this would introduce for our current scope, I directed it to use simple, native array storage instead.
3. **Dependency Control:** The AI repeatedly attempted to import external libraries (such as `moment.js`) for simple date calculations. Human oversight ensured we relied on clean native JavaScript `Date` methods instead of bloating the project's dependency tree.

In summary, leveraging AI as a supportive assistant while maintaining strict human governance ensured high output speed without sacrificing architectural simplicity or scope control.