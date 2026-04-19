# AI-Based Digital Behavior Analyzer Using Browser Activity Data

An intelligent browser activity analytics system that extracts Chrome browsing history, analyzes user behavior, classifies browsing patterns into productivity categories, calculates productivity insights, and visualizes results through an interactive dashboard.

This project was developed as a student-level applied AI + data analytics project using real browser history data from Windows Chrome profiles.

---

## 🚀 Overview

Many users spend hours online without understanding whether their browsing behavior is productive or distracting.

This project converts passive browser history into meaningful insights such as:

* Productivity Score
* Category-wise browsing analysis
* Top visited websites/pages
* User behavior summary
* Visual analytics dashboard

---

## ✨ Key Features

* Extracts Chrome browser history from local Windows system
* Reads Chrome SQLite history database
* Cleans and preprocesses raw browsing data
* Categorizes browsing activity into useful classes
* Calculates productivity score
* Stores processed data in MySQL
* Interactive dashboard using Streamlit
* Charts for behavior insights
* Optional AI API support for smart classification and summaries

---

## 🧠 Categories Used

The browsing data can be classified into categories such as:

* Learning
* Career
* Productivity
* Social Media
* Entertainment
* Shopping
* Utility
* News
* Unknown

---

## 📊 Productivity Score Logic

```text
(Productive Visit Count / Total Visit Count) × 100
```

Where productive categories may include:

* Learning
* Career
* Productivity
* Utility

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Databases

* SQLite (Chrome source data)
* MySQL (processed storage)

### Libraries Used

* pandas
* streamlit
* plotly
* mysql-connector-python
* sqlite3
* shutil
* python-dotenv

### Optional AI Support

* Google Gemini API

---

## ⚙️ Project Workflow

```text
Chrome History File
        ↓
SQLite Data Extraction
        ↓
Data Cleaning
        ↓
Category Classification
        ↓
CSV Export
        ↓
MySQL Storage
        ↓
Dashboard Visualization
        ↓
AI Insights (Optional)
```

---

## 📈 Dashboard Outputs

* Total Records
* Total Visits
* Unique Categories
* Productivity Score
* Category Distribution Pie Chart
* Top Visited Titles
* AI Behavior Summary
* Full Processed Data Table

---

## 📁 Folder Structure

```text
project/
│── app.py
│── extract_history.py
│── database.py
│── ai_utils.py
│── requirements.txt
│── .env
│── data/
│   └── history_processed.csv
```

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd project-folder
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
MYSQL_PASSWORD=your_password
GEMINI_API_KEY=your_key
```

### 5. Run Dashboard

```bash
streamlit run app.py
```

---

## ⚠️ Limitations

* Current classification may rely partly on rule-based logic
* Shared system profiles may mix user behavior
* Visit count does not always equal actual focus time
* AI API quota limitations may apply
* Chrome-specific implementation in current version

---

## 🔮 Future Improvements

* Multi-profile support
* Better AI categorization engine
* Weekly productivity reports
* Multi-browser support
* Offline local AI model integration
* Advanced time/session analytics

---

## 📚 Research Use Cases

This project can be extended for:

* Productivity analytics research
* Digital behavior analysis
* Student focus monitoring
* Web usage mining
* AI-assisted recommendation systems

---

## 👨‍💻 Author

Developed as a student learning + research project for practical experience in:

* Data Engineering
* Python Development
* SQL Databases
* API Integration
* AI Workflows
* Dashboard Development

---

## 📄 License

For educational and research purposes.
