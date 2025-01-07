import sys
import os
# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.model_loader import load_model
from src.data_preprocessor import preprocessor_data

def main():
    # Load the model
    model_path = "models/trained_model_2025-01-02.joblib"
    model = load_model(model_path)
    print("paso la carga del modelo")

    # Sample prediction
    input_data = {
        "Pregnancies": 6,
        "Glucose": 148,
        "BloodPressure": 72,
        "SkinThickness": 0,
        "Insulin": 0,
        "BMI": 33.6,
        "DiabetesPedigreeFunction": 0.627,
        "Age": 50
    }
    # columns to use
    columns_to_use=['BloodPressure', 'SkinThickness', 'BMI','Glucose','Insulin']
    # reply preprocessor of the training 
    preprocessed_data = preprocessor_data(data=input_data, columns_to_impute=columns_to_use)
    print("hizo el preprocesamiento con éxito")
    
    try: 
        prediction = model.predict(preprocessed_data)
        print(f"Predictions: {prediction}")
    except Exception as e:
        print(f"Error running inference: {e}")
        sys.exit(1)
    

if __name__ == "__main__":
    main()