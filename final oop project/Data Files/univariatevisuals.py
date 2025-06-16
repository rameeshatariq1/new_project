import matplotlib.pyplot as plt
import seaborn as sns

class UnivariatePlots:
    """
    Parameters:
        df: pd.DataFrame - cleaned dataset

    Functionality:
        - Plots histogram for each numeric column
        - Shows descriptive statistics
    """
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def plot_histogram(self, column, figsize=(8, 4), bins=30, color='skyblue', edgecolor='black' ):
        print(f"\nHistogram for '{column}'")
        plt.figure(figsize = figsize)
        plt.hist(self.df[column], bins=bins, color = color, edgecolor=edgecolor)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def plot_boxplot(self, column, figsize=(6, 4),color='salmon'):
        print(f"\nBoxplot for '{column}'")
        plt.figure(figsize = figsize)
        sns.boxplot(y=self.df[column], color=color)
        plt.title(f'Boxplot of {column}')
        plt.tight_layout()
        plt.show()

    def plot_kde(self, column, figsize=(8, 4), shade=True, color='purple'):
        print(f"\nKDE Plot for '{column}'")
        plt.figure(figsize = figsize)
        sns.kdeplot(self.df[column], shade= shade, color= color)
        plt.title(f'KDE (Density) Plot of {column}')
        plt.xlabel(column)
        plt.tight_layout()
        plt.show()

    def plot_countplot(self, column, figsize=(6, 4), palette='Set2'):
        print(f"\nCountplot for '{column}'")
        plt.figure(figsize = figsize)
        sns.countplot(x=self.df[column], palette=palette)
        plt.title(f'Countplot of {column}')
        plt.tight_layout()
        plt.show()
