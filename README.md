# 💰 Financial Tracker

A simple command-line personal finance tracker written in Python. It lets you manage a single user account and log financial transactions stored in a local SQLite database.

---

## 📋 Features

- **User authentication** — Create, login, and delete a user account (stored in a local CSV file)
- **Add transactions** — Record purchases with a name, description, amount, and automatic date
- **View transactions** — Display all transactions in a formatted table
- **Delete transactions** — Remove a transaction by name
- **Colorful CLI** — Color-coded menus using `colorama`
- **Tabular output** — Clean table display using `tabulate`

---

## 🗂️ Project Structure

```
Financial-Tracker/
├── main.py                  # Entry point — menus and transaction logic
├── requirements.txt         # Python dependencies
├── finance.db               # SQLite database (auto-created on first run)
├── id.csv                   # User credentials file (auto-created on first run)
└── Identification/
    ├── __init__.py
    └── id.py                # Identification class — handles user CRUD via CSV
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:danielbarseghian/Financial-Tracker.git
   cd Financial-Tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

```bash
python main.py
```

### Login Menu

| Option | Action |
|--------|--------|
| 1 | Login to an existing account |
| 2 | Create a new account *(only one account allowed at a time)* |
| 3 | Delete the current account and all associated data |
| 4 | Quit |

### Main Menu (after login)

| Option | Action |
|--------|--------|
| 1 | Add a new transaction |
| 2 | Show all transactions |
| 3 | Delete a transaction by name |
| 4 | Quit |

---

## 🗄️ Database

Transactions are stored in a local SQLite file (`finance.db`) with the following schema:

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto-generated 10-digit random ID |
| `name` | TEXT | Name of the purchase |
| `date` | TEXT | Date of the transaction (auto-filled) |
| `description` | TEXT | Short description |
| `amount` | REAL | Transaction amount |

---

## 🔐 Authentication

User credentials are stored in a plain-text CSV file (`id.csv`). Only **one account** can exist at a time. To create a new account, the existing one must be deleted first.

> ⚠️ **Note:** Passwords are stored in plain text. This project is intended for local personal use only.

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `colorama` | Colored terminal output |
| `tabulate` | Formatted table display |

Install them with:
```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is open source and available for personal use.
