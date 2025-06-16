# **_Mobile Price Prediction Model_**

*_This project is a machine learning-based dashboard that predicts the **price of a mobile phone** based on its specifications such as **RAM, ROM, battery power, and ratings**._*

## **_Objective_**

*_To build a user-interactive Streamlit dashboard that:_*
- *_Trains a model using mobile specifications_*
- *_Predicts the price of a phone_*
- *_Visualizes the data using graphs_*
- *_Accepts user input to estimate mobile prices_*

## **_Dataset_**

*_The dataset used contains mobile phone specifications including:_*
- *_RAM (in GB)_*
- *_ROM (in GB)_*
- *_Battery Power (in mAh)_*
- *_Ratings_*
- *_Price (target)_*

## **_Technologies Used_**

- **_Python_**
- **_Pandas & NumPy_** for data handling
- **_Seaborn & Matplotlib_** for visualization
- **_Scikit-learn_** for ML model training
- **_Streamlit_** for building the dashboard

## **_How It Works_**

1. *_Loads and preprocesses the data_*
2. *_Trains a **Random Forest Regressor**_*
3. *_Evaluates model performance using **R² Score** and **MSE**_*
4. *_Allows users to input mobile specs_*
5. *_Predicts the mobile price instantly_*

## **_Dashboard Features_**

- *_Show raw dataset and descriptive statistics_*
- *_Graphs: histogram, countplot, boxplot, and heatmap_*
- *_Sidebar shows model performance_*
- *_Predicts price based on user inputs_*

## How to Run

1. *_Make sure you have Python installed_*
2. *_Install required libraries:_*
   ```bash
   pip install streamlit, pandas, numpy, scikit-learn, matplotlib, seaborn
