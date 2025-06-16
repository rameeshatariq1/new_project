import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error

# Page configuration
st.set_page_config(page_title="Mobile Price Prediction Dashboard", layout="wide")
st.title("Mobile Price Prediction Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("mobile price prediction.csv")
    return df.dropna()

df = load_data()

# Show dataset
if st.checkbox("Show Raw Dataset"):
    st.subheader("Raw Dataset")
    st.write(df)

if st.checkbox("Show Descriptive Statistics"):
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

if st.checkbox("Show Head"):
        st.subheader("Head")
        st.write(df.head())

if st.checkbox("Show Tail"):
        st.subheader("Tail")
        st.write(df.tail())

if st.checkbox("Show Sample"):
        st.subheader("Sample")
        st.write(df.sample())

# Sidebar controls
st.sidebar.title("Graph Controls")
show_hist = st.sidebar.checkbox("Histogram of Key Features")
show_countplot = st.sidebar.checkbox("Countplot of Ratings")
show_boxplot = st.sidebar.checkbox("Boxplot: ROM vs Price")
show_heatmap = st.sidebar.checkbox("Correlation Heatmap")

# Histogram
if show_hist:
    st.subheader("Distribution of Features")
    num_cols = ['RAM', 'ROM', 'Price', 'Battery_Power']
    fig, axs = plt.subplots(2, 2, figsize=(14, 8))
    axs = axs.ravel()
    for i, col in enumerate(num_cols):
        axs[i].hist(df[col], bins=20, color='green', edgecolor='black')
        axs[i].set_title(col)
    st.pyplot(fig)

# Countplot
if show_countplot and 'Ratings' in df.columns:
    st.subheader("Countplot of Ratings")
    fig = plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x="Ratings", palette="Set2")
    st.pyplot(fig)

# Boxplot
if show_boxplot:
    st.subheader("Boxplot of ROM vs Price")
    fig = plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x="RAM", y="Ratings", palette="Set3")
    st.pyplot(fig)

# Correlation Heatmap
if show_heatmap:
    st.subheader("Feature Correlation Heatmap")
    fig = plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot(fig)

# Preprocessing
features = ['RAM', 'ROM', 'Battery_Power', 'Ratings']
target = 'Price'

X = df[features]
y = df[target]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Sidebar: Show model performance
st.sidebar.markdown("## Model Performance")
st.sidebar.metric("R² Score", f"{r2:.2f}")
st.sidebar.metric("Mean Squared Error", f"{mse:.2f}")

# User Input Section
st.header("Predict Mobile Price Based on Specs")

def user_input_features():
    ram = st.slider("RAM (in GB)", 1, 32, 8)
    rom = st.slider("ROM (in GB)", 4, 512, 64)
    power = st.slider("Battery Power (mAh)", 1000, 7000, 4000)
    rating = st.selectbox("Ratings", sorted(df['Ratings'].dropna().unique().tolist()))

    features = np.array([[ram, rom, power, rating]])
    scaled = scaler.transform(features)
    return scaled

input_data = user_input_features()

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Mobile Price: Rs.{prediction[0]:,.2f}")

