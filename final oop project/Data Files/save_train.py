import pickle
class PickleHandler:
    """
    A class to save and load machine learning models using pickle.
    
    Parameters:
    -----------
    model : object, optional
        Trained model object (e.g., LinearRegression, DecisionTree, etc.)
    
    Methods:
    --------
    save_model(filename):
        Saves the model to a specified .pkl file.
    
    load_model(filename):
        Loads and returns the model from a specified .pkl file.
    """
    def __init__(self, model=None):
        self.model = model

    def save(self, filename='mobile_price_model.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.model, f)
        return f"Model saved as {filename}"

    def load(self, filename='mobile_price_model.pkl'):
        with open(filename, 'rb') as f:
            self.model = pickle.load(f)
        return self.model