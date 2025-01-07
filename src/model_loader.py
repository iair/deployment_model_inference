import joblib

def load_model(model_path:str)->object:
    """
    Load the model from the specified path.

    Args:
        model_path (str): The path to the model file.

    Returns:
        The loaded model.
    """
    
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise