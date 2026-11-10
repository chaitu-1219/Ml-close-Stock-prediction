
# 📈 Stock Price Prediction Using Machine Learning

## Project Overview

This project focuses on predicting the closing price of Bharat Bond using Machine Learning regression algorithms.

The project uses historical 15-minute stock market data and applies Exploratory Data Analysis (EDA), data preprocessing, model training, and model evaluation.

A Streamlit web application is developed to allow users to enter market information and obtain predicted closing prices.

## Dataset

**Dataset:** BHARATBOND-APR30_15minute.csv

The dataset contains historical stock market information recorded at 15-minute intervals.

### Features Used

| Feature | Description |
|---|---|
| open | Opening price |
| high | Highest price |
| low | Lowest price |
| close | Actual closing price (Target) |

### Target Variable

`close`

### Independent Variables

- open
- high
- low

## Exploratory Data Analysis (EDA)

The following EDA techniques were performed:

- Dataset inspection using info() and describe()
- Missing value analysis
- Duplicate value detection
- Statistical analysis
- Feature distribution analysis
- Outlier detection using boxplots
- Correlation analysis
- Scatter plot analysis
- Stock price trend visualization
- Time-based analysis

## Machine Learning Algorithms

Three regression algorithms were implemented and compared:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

## Model Evaluation

The models were evaluated using:

- Mean Squared Error (MSE)
- R² Score

### Model Comparison

| Algorithm | MSE | R² Score |
|---|---:|---:|
| Linear Regression | 0.000008 | 0.9999997 |
| Decision Tree | 0.004001 | 0.9998477 |
| Random Forest | 0.002263 | 0.9999139 |

**Selected Model:** Random Forest Regressor

The Random Forest model was saved using Joblib.

## Project Structure

```text
Ml-close-Stock-prediction/
│
├── app.py
│
├── model/
│   └── stock_price_model.pkl
│
├── notebooks/
│   └── pro1.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Ml-close-Stock-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### 5. Open the Application

Visit:

http://localhost:8501

## Model Deployment

The application uses a pre-trained Random Forest Regressor model stored at:

`model/stock_price_model.pkl`

The model is loaded using Joblib and used to generate closing price predictions from user inputs.

## Future Improvements

- Add historical stock price charts.
- Implement time-series forecasting.
- Experiment with XGBoost and other regression algorithms.
- Improve model generalization.
- Deploy the application online.
- Add interactive stock market visualizations.

## Disclaimer

This project is developed for educational purposes.

The predictions are model estimates and should not be considered financial advice.

## Author

Chaitanya