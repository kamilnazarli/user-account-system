# 🛡️ User Account System (Python)

A simple object-oriented user login system built with Python.  
This project includes:

- Password validation (length, digit, uppercase)
- Login attempts tracking
- Account lockout after 3 failed logins
- Time-based unlock (after 60 seconds)
- Secret answer–based password reset
- Username update
- Login history tracking
- File-based logging of events

## 🔧 Features
- Encapsulation using `__private` and `_protected`
- Time management with `datetime`
- File logging with `log.txt`
- Clean and readable OOP structure

## 🚀 How to Run

1. Clone or download this repo.
2. Run the Python file:
```bash
python user_account_system.py
## ✅ Example Output
1.Login
2.Update Password
3.Reset Password
4.Show Login History
5.Exit
Choose an option: 1
Enter your password: wrongpass
Incorrect password
Choose an option: 1
Enter your password: wrongpass
Incorrect password
Choose an option: 1
Enter your password: wrongpass
Account is locked due to too many failed attempts. Wait at least one minute.```

## 📄 Log File

The `log.txt` file automatically stores login and system event logs such as:

- Successful and failed login attempts
- Password updates and resets
- Account lockouts and unlocks

This file is useful for tracking user activity and debugging.

> Note: If you're running this program locally, a new `log.txt` will be created in the project directory if it doesn't already exist.

