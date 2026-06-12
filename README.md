# 🔐 Secure Password Generator

A simple Python-based Secure Password Generator that creates strong and random passwords. The generated password contains a mix of uppercase letters, lowercase letters, numbers, and special characters to improve security.

## 🚀 Features

* User-defined password length
* Ensures at least:

  * 1 Uppercase letter
  * 1 Lowercase letter
  * 1 Number
  * 1 Special character
* Randomly shuffles characters for better security
* Input validation for password length
* Handles invalid inputs gracefully

## 🛠️ Technologies Used

* Python 3
* `random` module
* `string` module

## 📂 Project Structure

```text
SecurePasswordGenerator/
│
├── password_generator.py
└── README.md
```

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/secure-password-generator.git
```

### Step 2: Navigate to the Project Directory

```bash
cd secure-password-generator
```

### Step 3: Run the Program

```bash
python password_generator.py
```

## 📖 Usage

When the program starts:

```text
=== SECURE PASSWORD GENERATOR ===
```

Enter the desired password length:

```text
Enter password length (minimum 4): 12
```

Example Output:

```text
Generated Password:
A$8kP2!mQ7xL
```

## 💡 Example

### Input

```text
Enter password length (minimum 4): 10
```

### Output

```text
Generated Password:
g@7Kq9#Lp2
```

## 🔒 Password Rules

The generated password always includes:

| Character Type    | Example                |
| ----------------- | ---------------------- |
| Uppercase Letter  | A, B, C                |
| Lowercase Letter  | a, b, c                |
| Number            | 1, 2, 3                |
| Special Character | !, @, #, $, %, ^, &, * |

Minimum password length allowed: **4 characters**

## ⚠️ Error Handling

If the user enters a length less than 4:

```text
Password length must be at least 4.
```

If the user enters a non-numeric value:

```text
Please enter a valid number only.
```

## 🔮 Future Enhancements

* Copy password to clipboard
* Save generated passwords to a file
* User-selectable special characters
* Password strength meter
* GUI version using Tkinter
* Generate multiple passwords at once

## 🎯 Learning Outcomes

This project helps practice:

* Python Lists
* Randomization
* String Manipulation
* Exception Handling
* User Input Validation
* Built-in Python Modules

## 👨‍💻 Author

Created as a beginner-friendly Python project to learn random password generation and security best practices.

## 📜 License

This project is open-source and free to use for educational and personal purposes.
