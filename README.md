# House-Price-Predictor

## 📌 Project Overview
This project involves analyzing real estate data from Zameen.com to predict house prices using machine learning models. The dataset `zameen-updated.csv` contains real estate listings with features such as area, location, price, number of bedrooms, and more. The goal is to build a predictive model and deploy it using Streamlit for interactive use.

## 🎯 Objectives
- Clean and preprocess real estate data.
- Perform exploratory data analysis (EDA) to identify trends and outliers.
- Engineer relevant features to improve model performance.
- Train and evaluate multiple regression models.
- Tune hyperparameters for optimal performance.
- Predict future property prices.
- Deploy a user-friendly web app using Streamlit.

## 🛠️ Methodology

### 1. Data Preprocessing
- Handled missing values and duplicates.
- Converted categorical variables using label encoding and one-hot encoding.
- Removed outliers based on price and area.
- Feature scaling using StandardScaler.

### 2. Exploratory Data Analysis
- Visualized distributions of prices, locations, and features.
- Correlation heatmaps and box plots for insight into influential variables.

### 3. Feature Engineering
- Created new features like `price_per_marla`.
- Applied log transformation to reduce skewness.

### 4. Model Building
- Trained Linear Regression, Random Forest, XGBoost, and Gradient Boosting models.
- Performed cross-validation and hyperparameter tuning using GridSearchCV.

### 5. Model Evaluation
- Used metrics like MAE, RMSE, and R² to compare model performance.
- Selected the best-performing model based on validation scores.

### 6. Deployment
- Built an interactive web app using **Streamlit**.
- App allows users to input property details and get price predictions.

## 📁 Project Structure

```
📦House-Price-Prediction
 ┣ 📂data
 ┃ ┗ 📄zameen-updated.csv
 ┣ 📂notebooks
 ┃ ┗ 📄house_price_modeling.ipynb
 ┣ 📂models
 ┃ ┗ 📄best_model.pkl
 ┣ 📂streamlit_app
 ┃ ┗ 📄app.py
 ┣ 📄README.md
 ┣ 📄requirements.txt
 ┗ 📄report.docx
```

## ✅ Requirements

See `requirements.txt` for full details. Key libraries include:
- pandas
- numpy
- matplotlib / seaborn
- scikit-learn
- xgboost
- streamlit
- joblib

## 📊 Results

- The Random Forest model performed the best with R² > 0.85 on validation data.
- The deployed model can reliably estimate house prices based on user inputs.
