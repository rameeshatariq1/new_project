import matplotlib.pyplot as plt
import seaborn as sns
class BivariatePlots:
    """
    Parameters:
        df: pd.DataFrame - cleaned dataset

    Functionality:
        - Plots correlation heatmap
        - Plots scatterplots between key pairs
    """
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def scatter_plot(self, col1, col2, figsize=(8, 5), palette='coolwarm'):
        print(f"\nScatter Plot: '{col1}' vs '{col2}'")
        plt.figure(figsize=figsize)
        sns.scatterplot(x=self.df[col1], y=self.df[col2], hue=self.df['RAM'], palette=palette)
        plt.title(f'Scatter Plot: {col1} vs {col2}')
        plt.tight_layout()
        plt.show()

    def correlation_heatmap(self, figsize=(10, 8), annot=True, cmap='coolwarm', fmt=".2f", square=True):
        print("\nCorrelation Heatmap")
        plt.figure(figsize=figsize)
        sns.heatmap(self.df.corr(), annot=annot, cmap=cmap, fmt=fmt, square=square)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    def boxplot_by_category(self, numerical_col, category_col='RAM',figsize=(7, 5), palette='pastel'):
        print(f"\nBoxplot: '{numerical_col}' grouped by '{category_col}'")
        plt.figure(figsize=figsize)
        sns.boxplot(x=self.df[category_col], y=self.df[numerical_col], palette=palette)
        plt.title(f'Boxplot of {numerical_col} by {category_col}')
        plt.tight_layout()
        plt.show()

    def pairplot(self, columns=None , hue='RAM', palette='husl'):
        print(f"\nPairplot of selected features")
        if columns:
            sns.pairplot(self.df[columns], hue=hue, palette=palette)
        else:
            sns.pairplot(self.df, hue=hue, palette=palette)
        plt.tight_layout()
        plt.show()