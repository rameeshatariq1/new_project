class UnivariateAnalysis:
    """This class analyzes one variable at a time, showing distribution
    through histograms and descriptive stats."""
    
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def unique_counts(self, column):
        print(f"\nUnique values in '{column}':")
        print(self.df[column].nunique())

    def value_counts(self, column):
        print(f"\nValue counts in '{column}':")
        print(self.df[column].value_counts())

    def column_summary(self, column):
        print(f"\nSummary statistics for '{column}':")
        print(self.df[column].describe())

    def check_skewness(self, column):
        print(f"\nSkewness of '{column}': {self.df[column].skew()}")

    def check_kurtosis(self, column):
        print(f"\nKurtosis of '{column}': {self.df[column].kurt()}")