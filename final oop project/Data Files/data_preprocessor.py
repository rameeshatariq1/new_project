class DataCleaner:
    """
    Cleans and preprocesses the dataset:
    - Removes duplicates
    - Handles missing values
    - Renames long column names
    - Converts data types if needed
    """
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def check_nulls(self):
        print("\nChecking for null values:")
        print(self.df.isnull().sum())

    def replace_zeros(self):
        print("\nHandling zero values in selected columns...")
        """
        Columns where 0 is not a valid value
        """
        cols_with_invalid_zeros = ['RAM','ROM','Mobile_Size','Primary_Cam','Selfi_Cam','Battery_Power']

        for col in cols_with_invalid_zeros:
            zero_count = (self.df[col] == 0).sum()
            print(f"Column '{col}' has {zero_count} zero values.")
            """
            Replace zeros with median of the column
            """
            median_value = self.df[col].median()
            self.df[col] = self.df[col].replace(0, median_value)
            print(f"Replaced zeros in '{col}' with median value: {median_value}")

    def rename_columns(self):
        """
        Replaces complex names with simple names.
        """
        print("\nRenaming columns to simpler names...")
        renamed_columns = {
            'Mobile_Size': 'mblSize',
            'Primary_Cam': 'priCam',
            'Selfi_Cam': 'selCam',
            'Battery_Power': 'power',
        }
        self.df.rename(columns=renamed_columns, inplace=True)
        print("Renamed columns successfully.")

    def get_clean_data(self):
        return self.df
