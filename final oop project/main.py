from Code.data_load import DataLoader
from Code.data_preprocessor import DataCleaner
from Code.statistical import StatisticalSummary
from Code.univariateanalysis import UnivariateAnalysis
from Code.bivariateanalysis import BivariateAnalysis
from Code.univariatevisuals import UnivariatePlots
from Code.bivariatevisuals import BivariatePlots
from Code.ml_workflow import DataSplitter
from Code.ml_workflow import ModelTrainer
from Code.ml_workflow import ModelEvaluator
from Code.ml_workflow import ModelPredictor
from Code.save_train import PickleHandler

def main():
    """Initialize DataLoader Object with CSV File"""
loader = DataLoader("mobile price prediction.csv")
print(loader.load_data())
print(loader.show_head())
print(loader.show_tail())
print(loader.show_sample())
print(loader.show_description())
print(loader.show_info())

"""
Assuming df is already loaded
"""
loader = DataLoader("mobile price prediction.csv")
loader.load_data()
df = loader.df
cleaner = DataCleaner(df)
cleaner.check_nulls()
cleaner.replace_zeros()
cleaner.rename_columns()

"""Get the cleaned and updated dataframe
"""
cleaned_df = cleaner.get_clean_data()

stats = StatisticalSummary(cleaned_df)
print(stats.show_mean())
print(stats.show_median())
print(stats.show_mode())
print(stats.show_max())
print(stats.show_min())
print(stats.show_std())
print(stats.show_variance())
print(stats.show_count())

uni = UnivariateAnalysis(cleaned_df)
uni.unique_counts('RAM')
uni.value_counts('Ratings')
uni.column_summary('ROM')
uni.check_skewness('power')
uni.check_kurtosis('Price')


bi = BivariateAnalysis(cleaned_df)
bi.correlation_matrix()
bi.covariance_matrix()
bi.group_mean_by_target('RAM')
bi.group_count_by_target('RAM')
bi.crosstab_two_columns('RAM', 'ROM')

# Step 0: Assume cleaned_df already exists
splitter = DataSplitter(cleaned_df)
X_train, X_test, y_train, y_test = splitter.split()

# Step 1: Train
trainer = ModelTrainer()
model = trainer.train_model(X_train, y_train)

# Step 2: Evaluate
evaluator = ModelEvaluator(model)
results = evaluator.evaluate(X_test, y_test)
print("Accuracy:", results["accuracy"])
print("Confusion Matrix:\n", results["confusion_matrix"])
print("Classification Report:\n", results["classification_report"])

# Step 3: Predict
predictor = ModelPredictor(model)
sample = X_test.sample(1)
print("Prediction on sample row:", predictor.predict(sample))


saver = PickleHandler(model)
print(saver.save())

# Optional: To load later
loaded_model = saver.load()

uni_plot = UnivariatePlots(cleaned_df)

uni_plot.plot_histogram('RAM')
uni_plot.plot_boxplot('ROM')
uni_plot.plot_kde('Price')
uni_plot.plot_countplot('Ratings')


bi_plot = BivariatePlots(cleaned_df)

bi_plot.scatter_plot('Price', 'RAM')
bi_plot.correlation_heatmap()
bi_plot.boxplot_by_category('Ratings')


if __name__ == "__main__":
    main()
