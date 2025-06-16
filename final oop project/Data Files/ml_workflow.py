from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, r2_score
# 1. Data Splitting
class DataSplitter:
    """
    Parameters:
        df: pd.DataFrame - cleaned dataset

    Functionality:
        - Splits dataset into train/test sets

    Returns:
        - X_train, X_test, y_train, y_test
    """
    def __init__(self, dataframe, target_column='RAM', test_size=0.2, random_state=42):
        self.df = dataframe
        self.target = target_column
        self.test_size = test_size
        self.random_state = random_state

    def split(self):
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )
        return X_train, X_test, y_train, y_test


# 2. Model Training
class ModelTrainer:
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model


# 3. Model Evaluation
class ModelEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        return {
            "accuracy": acc,
            "confusion_matrix": cm,
            "classification_report": report
        }


# 4. Model Prediction
class ModelPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, new_data_df):
        return self.model.predict(new_data_df)
