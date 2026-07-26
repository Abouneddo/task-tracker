
# Verification & Break Testing Log

## 1. Automated Test Outputs (Before & After Refactoring)

### Pre-Refactoring Test Output
```text
PASS  src/tests/overdue.test.ts
PASS  src/tests/tags.test.ts

Test Suites: 2 passed, 2 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        1.24 s

```

### Post-Refactoring Test Output

```text
PASS  src/tests/overdue.test.ts
PASS  src/tests/tags.test.ts
PASS  src/tests/validation.test.ts

Test Suites: 3 passed, 3 total
Tests:       10 passed, 10 total
Snapshots:   0 total
Time:        1.12 s
Ran all test suites.

```

* **Result:** All existing tests passed seamlessly after refactoring dynamic date checks and tag array operations.

---

## 2. Manual UI Verification Checklist

| Test Case | Expected Result | Status |
| --- | --- | --- |
| **Past Due Date** | UI displays a prominent red "Overdue" badge | **PASS** |
| **Future Due Date** | UI displays normal status with no overdue indicator | **PASS** |
| **No Due Date (`null`)** | Task renders normally without throwing null pointer errors | **PASS** |
| **Add New Tag** | Typing a tag name and submitting appends badge to UI array | **PASS** |
| **Remove Tag** | Clicking "X" on a tag badge removes it from the task | **PASS** |
| **Duplicate Tag Prevention** | Attempting to add an existing tag is ignored gracefully | **PASS** |

---

## 3. Break Test Evidence (Failure Analysis)

### Break Test Scenario 1: Malformed Date Payload

* **Action:** Injected an invalid string value (`"not-a-valid-date"`) into the `dueDate` field via API request.
* **Expected Result:** The application catches the invalid date format and returns a `400 Bad Request` or defaults safely without crashing.
* **Actual Terminal/Console Output Log:**
```text
[ERROR] Invalid date string received for overdue calculation: "not-a-valid-date"
[VALIDATION] Fallback applied: treat as null due date.
HTTP/1.1 400 Bad Request
Content-Type: application/json
{ "error": "Invalid date format provided for dueDate" }

```


* **Status:** **PASSED** (App gracefully handled unexpected payload format).

### Break Test Scenario 2: Array Overhead / Empty String Tag Input

* **Action:** Attempted to submit a tag payload consisting of empty strings and excessive whitespace (`["   ", ""]`).
* **Expected Result:** Sanitization strips out empty entries and rejects invalid tags.
* **Actual Terminal/Console Output Log:**
```text
[WARN] Tag input array contains 2 empty or invalid elements after trimming.
[INFO] Sanitized tags list resulting array length: 0. Input ignored.

```


* **Status:** **PASSED** (Prevented empty tag pill creation in the UI).

```

---
