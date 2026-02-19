# 🧠 HENNGE Admission Challenge Solution

This repository contains my solution to the HENNGE Engineering Challenge, written in Python. The task processes multiple test cases and computes the sum of the fourth powers of all non-positive integers per case.


## 📜 Problem Summary

Each test case:
- Starts with a single integer `X`
- Followed by `X` space-separated integers

For each test case:
- Extract only **non-positive** integers (≤ 0)
- Compute the **sum of their 4th powers**
- If input is invalid or missing, return `-1`

---

## ✅ Constraints Followed

| Constraint                              | Followed? |
|----------------------------------------|-----------|
| No `for` or `while` loops              | ✅ Yes     |
| No list/set/dictionary comprehensions  | ✅ Yes     |
| Input must be read via `sys.stdin`     | ✅ Yes     |
| Output must only appear at the end     | ✅ Yes     |
| Solution in a **single file**          | ✅ Yes     |

---

## 🛠️ Implementation Highlights

- Functional programming style using recursion
- Gracefully handles invalid input by returning `-1`
- Clean, readable, and extensible codebase
- No third-party libraries used

---

## 🚀 How to Run

Use standard input redirection to run the program:

```bash
python main.py 
```
