import numpy as np
import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        """
        Initializes the DataLoader with file path
        Loads data into self.df
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            return "Data loaded successfully."
        except Exception as e:
            print(f"Error loading data: {e}")

    def show_head(self):
        """Returns the first 5 rows of the dataset"""
        print("\nHead of the dataset:")
        return self.df.head()

    def show_tail(self):
        """Returns the last 5 rows of the dataset"""
        print("\nTail of the dataset:")
        return self.df.tail()

    def show_sample(self):
        """Returns a random sample of n rows"""
        print("\nRandom sample of the dataset:")
        return self.df.sample(5)

    def show_description(self):
        """Returns statistical description of the dataset"""
        print("\nStatistical summary:")
        return self.df.describe()

    def show_info(self):
        """Prints information about the dataset"""
        print("\nDataset information:")
        return self.df.info()
loader = DataLoader("mobile price prediction.csv")
loader.load_data()