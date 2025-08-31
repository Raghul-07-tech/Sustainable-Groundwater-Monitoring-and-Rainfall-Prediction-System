# Sustainable Groundwater & Rainfall Prediction System (week 1)

## 📌 Project Title
**Sustainable Groundwater & Rainfall Prediction System**

---

## 📖 Introduction
Groundwater is one of the most critical natural resources for sustaining agriculture, industry, and human consumption. This project focuses on **analyzing groundwater depth variations** and building a **rainfall-groundwater prediction system** to help in **sustainable water management**.  

The dataset used in this project provides **changes in depth to water levels** across different states in India, obtained from the **State Groundwater Boards**.

---

## 🎯 Aim
- To preprocess and analyze groundwater dataset.  
- To clean missing values, handle outliers, and standardize data.  
- To build a **sustainable groundwater prediction model** using machine learning.  
- To provide useful insights for **rainfall and groundwater level prediction**.

---

## 📂 Dataset
- **Path**: `C:\Users\moort\Downloads\state-groundwater-boards-changes-in-depth-to-water-level.csv`
- **Description**: Contains groundwater depth variations across states and years.

---

## ⚙️ Preprocessing Steps
1. **Import libraries** – pandas, numpy, matplotlib, seaborn, sklearn.  
2. **Load dataset** – read CSV file from given path.  
3. **Data cleaning** – handle missing values (imputation/removal).  
4. **Remove duplicates** – ensure unique records.  
5. **Handle outliers** – remove or cap extreme values using IQR method.  
6. **Feature engineering** – create new features if required.  
7. **Encoding** – convert categorical data (state names, etc.) into numerical form.  
8. **Scaling** – normalize features using MinMaxScaler or StandardScaler.  
9. **Split dataset** – train-test split (80%-20%).  
10. **Save preprocessed data** – store cleaned dataset for model training.

---

## 🛠️ Technologies Used
- **Python 3**
- **Pandas & NumPy** – Data preprocessing
- **Matplotlib & Seaborn** – Visualization
- **Scikit-learn** – Machine learning preprocessing tools

---

## 🚀 How to Run
1. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
