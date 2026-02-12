# 🗳️ Online Voting System (Python)

A **console-based Online Voting System** built using **Python, OOP concepts, and file handling**.  
This project simulates a real-world voting system with role-based access control for **Admin** and **Users**.

---

## 🚀 Features

### 👤 User Features
- User Registration with strong password validation
- Secure Login system
- View personal details
- Cast vote (only once)
- Prevent duplicate voting

### 👑 Admin Features
- Add candidates
- Remove candidates
- View election results

---

## 🔐 Password Security

The system enforces strong passwords:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

---

## 📂 File Structure

The system uses text files for persistent storage:

| File | Purpose |
|------|--------|
| `users.txt` | Stores user data |
| `candidates.txt` | Stores candidate names |
| `votes.txt` | Stores voting records |

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming (OOP)
- File Handling
- Regular Expressions (Regex)
- Git & GitHub

---

## ▶️ How to Run

```bash
git clone https://github.com/DevSahil12/VotingSystem.git
cd VotingSystem
python voting_system.py
