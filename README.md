# 🍽️ RESTAURANT BILLING SYSTEM  
### Modern Billing System using Python, Tkinter & MySQL (v2.0)

The Restaurant Billing System is a Python-based desktop application designed to help restaurant staff take orders, calculate bills, store bill history, and print receipts.  
Version **2.0** introduces a modern UI, theme switching, MySQL storage, and major improvements over Version 1.0.

---

## ⭐ What's New in Version 2.0

- Modern UI using **ttkbootstrap** (Flatly + Darkly themes)
- **Dark / Light Mode Toggle** button
- Fully **auto-responsive layout** using `.grid()`
- **MySQL database integration** for storing bills
- **Search Bill** by Bill Number or Phone Number
- **View All Bills** table window
- Added **6 new Indian vegetarian food items**
- Cleaner Bill Area layout and reduced space gaps
- **Windows Print** support
- Save bill as **TXT file**
- Automatic bill number generation

---

## 🆚 Version Comparison (v1.0 vs v2.0)

| Feature | v1.0 | v2.0 |
|--------|------|-------|
| UI Framework | Basic Tkinter | Modern ttkbootstrap |
| Theme Mode | No | Yes (Dark + Light) |
| Layout System | `.place()` | `.grid()` (responsive) |
| Storage | CSV only | MySQL + CSV |
| Search Bills | No | Yes |
| View All Bills | No | Yes |
| Menu Items | Limited | +6 new items |
| Edit Bill | No | Added |
| Printing | Basic | Improved printing |
| Code Quality | Basic | Modular & scalable |

---

## 📸 Screenshots (v2.0)

### Main Application Window  
![v2_main](https://github.com/user-attachments/assets/c20cec59-70fe-43d9-b1f3-4c7f20a07fa1)

### Search Bills Window  
![v2_search](https://github.com/user-attachments/assets/14a9b668-d4bf-4280-a334-bbee64ecbc5d)

---

## 🖼️ Old UI (v1.0)

![v1_screenshot](https://github.com/JILSPATEL/restaurant-billing-system/assets/100358865/80eb676a-b2a9-4fe8-8e0f-64b38d598814)

---

## 🍽️ Features (v2.0)

- Customer details input (Name, Phone, Table Number)
- Menu categories:
  - Snacks
  - Specialities
  - Beverages
- Automatic calculations:
  - Item Total
  - GST (2.5%)
  - Final Bill Amount
- Bill preview area
- Save bill as **TXT file**
- Save bill to **MySQL database**
- Search bill by:
  - Bill Number  
  - Phone Number  
- View all bills (table format)
- Print bill (Windows)
- Dark/Light theme toggle
- Edit Bills 
- Auto-created `bills/` directory for receipts

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/JILSPATEL/restaurant-billing-system.git
cd restaurant-billing-system
```

### 2️⃣ Install Required Python Packages.
```bash
pip install ttkbootstrap
pip install mysql-connector-python
```

### 3️⃣ MySQL Setup
#### Make sure MySQL is installed (Windows or WSL).
```bash
mysql -u root -p
CREATE DATABASE rbs;
EXIT;
```
### ▶️ Run the Application
```bash
python rbs.py
```
### 📦 Project Structure

```
restaurant-billing-system/
├── rbs.py                    # main application
├── bills/                    # TXT receipts (auto-created)
├── README.md                 # documentation
└── RBS_v2_setup_guide.pdf    # setup guide
```


## 📁 Data Persistence

### ✔ MySQL Database Stores:
- Bill number  
- Customer name  
- Phone number  
- Table number  
- GST  
- Total bill amount  
- Date & time  

### ✔ CSV Backup
- `hotel.csv` is used as an additional offline storage file.
---

## 📚 Dependencies

- Python 3.x  
- tkinter (built-in)  
- ttkbootstrap  
- mysql-connector-python  
- csv  
- os  
- time  
- tempfile  
- pathlib  
- random  

> All modules are built-in except **ttkbootstrap** and **mysql-connector-python**.

---

## 👨‍💻 Author

**Jils Patel**  
Python & System Software Developer  
MTech CSE '27  

---

## ⭐ Support

If you find this project helpful, please consider **starring ⭐ the repository** on GitHub!

---

If you want:
- GitHub badges (stars, forks, Python version)  
- A README banner  
- Version 2.0 release notes  
- A LICENSE file  

Just tell me — I can generate them!
