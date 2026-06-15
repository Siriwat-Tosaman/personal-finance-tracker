# 💰 Personal Finance Tracker

A simple command-line program for tracking personal income and expenses, built with Python.

---

## 📸 Screenshots

### Add Record
```
Do you want to add a record or view records or search by category? (add/view/search) add
revenue or expense? revenue
How much? 5000
What category? salary
your revenue is 5000.0
Calculating totals...
Record added successfully.

Total Revenue: 5000.0
Total Expense: 0.0
========================================
======== Total Balance: 5000.0 =========
========================================
```

### View All Records
```
Do you want to add a record or view records or search by category? (add/view/search) view
====== revenue ======
Amount: 5000.0 Bath
Category:  salary
Date:  2026-06-15 10:00:00
====== expense ======
Amount: 600.0 Bath
Category:  food
Date:  2026-06-15 11:00:00

Total Revenue: 5000.0
Total Expense: 600.0
========================================
======== Total Balance: 4400.0 =========
========================================
```

### Search by Category
```
Do you want to add a record or view records or search by category? (add/view/search) search
Enter the category to search for: food
====== expense ======
Amount: 600.0 Bath
Category:  food
Date:  2026-06-15 11:00:00

Total Revenue for category 'food': 0.0
Total Expense for category 'food': 600.0
========================================
======== Total Balance for category 'food': -600.0 =========
========================================
```

---

## 📋 Features

- ➕ Add income (revenue) and expense records with category and timestamp
- 📄 View all records with a full summary
- 🔍 Search records by category
- 💾 Auto-save to `records.txt` — data persists after the program closes
- ⚠️ Error handling for invalid inputs

---

## 🛠️ Technologies

| Technology | Usage |
|---|---|
| Python 3 | Main programming language |
| `datetime` | Auto-generate timestamps |
| File I/O (`open`, `read`, `write`) | Save and load records from `.txt` file |
| Modular functions (`file_handler.py`) | Separate file handling logic from main program |

---

## 🔧 Functions

| Function | Description |
|---|---|
| `add_record()` | Write new record to `records.txt` |
| `view_records()` | Read all records from file |
| `summary()` | Show all records + total summary |
| `summary_add()` | Show total summary only (used after adding) |
| `summary_search()` | Filter and show records by category |

---

## 📁 Project Structure

```
Personal-Finance-Tracker/
├── main.py          # Main program — menu and user input
├── file_handler.py  # File I/O and summary logic
└── records.txt      # Data storage (auto-created on first add)
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone or download this repository
3. Run the program:

```bash
python main.py
```

4. Choose an option: `add`, `view`, or `search`

---

## 💡 Concepts Used

- `def` functions and modular code
- `while`-style input flow with `if/elif/else`
- File I/O with `open()` in append (`"a"`) and read (`"r"`) mode
- String manipulation: `split()`, `strip()`
- Exception handling: `try/except` for `ValueError`, `FileNotFoundError`, `TypeError`
