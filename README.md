
# 🌍 World Happiness Data Analysis Project

## 📌 Project Overview
This project is a **menu-driven Python application** designed to perform **data analysis, data cleaning, statistical operations, NumPy operations, aggregation, and data visualization** on the **World Happiness dataset**.

It helps users understand:
- How happiness scores vary across countries
- The relationship between happiness and GDP
- Data preprocessing and exploratory data analysis (EDA)
- Visualization using Matplotlib and Seaborn

This project is ideal for **Data Analysis / AI & ML students** as it combines **Pandas, NumPy, Matplotlib, and Seaborn** in one complete workflow.

---

## 🗂️ Project Structure
```
World_Happiness_Project/
│
├── FINAL_PROJECT_10.py        # Main Python program (menu-driven)
├── world_happiness.csv       # Dataset file (user provided)
├── README.md                 # Project documentation
```

---

## 🧰 Technologies Used
- **Python 3**
- **NumPy** – numerical operations
- **Pandas** – data manipulation and analysis
- **Matplotlib** – plotting graphs
- **Seaborn** – advanced data visualization

---

## 📊 Dataset Description
The dataset contains country-wise happiness information with columns such as:
- `Country`
- `OverallRank`
- `Score`
- `GDP per capita`
- `Social support`
- `Healthy life expectancy`
- `Freedom to make life choices`

---

## ⚙️ How to Run the Project
1. Install required libraries:
```bash
pip install numpy pandas matplotlib seaborn
```

2. Run the Python file:
```bash
python FINAL_PROJECT_10.py
```

3. Enter the **CSV file path** when prompted.

---

## 🧭 Main Menu Features
```
1. Load Dataset
2. Explore Data
3. Handle Missing Values
4. DataFrame & NumPy Operations
5. Data Visualization
6. Subplots
7. Exit
```

---

## 🔍 Module-wise Explanation

### 1️⃣ Load Dataset
- Loads the CSV file using Pandas
- Handles file not found errors

---

### 2️⃣ Explore Data
Allows basic exploration:
- First 5 rows
- Last 5 rows
- Column names
- Data types
- Dataset information

---

### 3️⃣ Data Cleaning
- Detect missing values
- Fill missing values using mean
- Replace missing values manually
- Detect duplicate rows
- Drop unnecessary columns

---

### 4️⃣ DataFrame & NumPy Operations

#### ➤ Convert DataFrame to NumPy
- Convert full dataset or selected columns into NumPy array

#### ➤ Indexing & Slicing
- Access elements and slices from NumPy array

#### ➤ Mathematical Operations
- Addition
- Subtraction
- Multiplication
- Division

#### ➤ Statistical Operations
- Mean
- Median
- Mode
- Correlation
- Standard Deviation
- Variance

#### ➤ Search Data
- Search a numeric value inside NumPy array

#### ➤ Sort Data
- Sort dataset based on a selected column

#### ➤ Aggregation Functions
- Country-wise average happiness score
- Country-wise min, max, mean score
- GDP analysis
- Pivot tables

---

## 📈 Data Visualization Features

### Graphs Included:
- **Bar Chart** – Top 10 happiest countries
- **Pie Chart** – Contribution of happiness factors
- **Line Chart** – Rank vs Happiness score
- **Scatter Plot** – GDP vs Happiness score
- **Histogram** – Score distribution
- **Heatmap** – Correlation matrix
- **Box Plot** – Happiness score spread

All visualizations use **Seaborn + Matplotlib**.

---

## 📊 Subplots Dashboard
A 2x3 grid showing:
- Top 10 happiest countries
- Pie chart of score share
- Rank vs Score
- GDP vs Score
- Histogram
- Box plot

---

## 🚀 Key Learning Outcomes
- Real-world data handling
- Exploratory Data Analysis (EDA)
- NumPy array operations
- GroupBy & Pivot tables
- Data visualization best practices
- Menu-driven Python programs

---

## 📝 Future Improvements
- Add exception handling for invalid inputs
- Export plots as image files
- Add interactive visualizations
- Improve filter/search functionality

---

## 👩‍💻 Author
**Rituu Poonjani**  
Data Analysis / AI & ML Student

---

## ✅ Conclusion
This project demonstrates a **complete data analysis pipeline**, from loading raw data to generating meaningful insights using statistical analysis and visualization. It is a strong foundation project for students learning **Data Analytics and Machine Learning basics**.
