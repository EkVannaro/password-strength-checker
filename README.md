# 🔐 Password Strength Checker

## Overview

The Password Strength Checker is a Python program that evaluates the strength of a password based on common cybersecurity best practices. It analyzes the password against several security rules, calculates a score, and provides feedback to help users create stronger passwords.

This project was built to practice Python programming while learning the fundamentals of password security.

---

## Features

* Check for a minimum password length of 8 characters
* Check for uppercase letters
* Check for lowercase letters
* Check for digits
* Check for special characters
* Detect commonly used passwords from a password list
* Reject empty password input
* Display a password score out of 5
* Classify passwords as Weak, Medium, or Strong
* Provide suggestions for improving password strength

---

## Technologies Used

* Python 3
* Regular Expressions (`re` module)

---

## Project Structure

```text
Password-Strength-Checker/
│── password_checker.py
│── common_passwords.txt
└── README.md
```

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/EkVannaro/password-strength-checker.git
```

2. Navigate to the project folder:

```bash
cd Password-Strength-Checker
```

3. Run the program:

```bash
python password_checker.py
```

---

## Example Output

### Example 1

```text
Enter password: password

Password was found in common list. Try another one.
```

### Example 2

```text
Enter password: hello

Score: 1/5
Weak Password!

Better password needs at least
8 characters
one uppercase
one digit
one special character
```

### Example 3

```text
Enter password: Hello123!

Score: 5/5
Strong Password!

Valid!
```

---

## Password Strength Rules

| Rule              | Requirement                                 |
| ----------------- | ------------------------------------------- |
| Length            | At least 8 characters                       |
| Uppercase         | At least one uppercase letter               |
| Lowercase         | At least one lowercase letter               |
| Digit             | At least one number                         |
| Special Character | At least one special character (`!@#$%^&*`) |
| Common Password   | Must not appear in the common password list |

---

## What I Learned

Through this project, I gained experience with:

* Python functions
* Conditional statements
* Loops
* Lists
* File handling
* Regular expressions
* Password validation techniques
* Basic cybersecurity concepts related to password security

---

## Future Improvements

* Hide password input using the `getpass` module
* Generate secure random passwords
* Estimate password entropy
* Support a wider range of special characters
* Build a graphical user interface (GUI)