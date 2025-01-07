import pandas as pd
import numpy as np

def preprocessor_data(data:dict, columns_to_impute:list)->pd.DataFrame:
    
    
    try:
        df = pd.DataFrame([data])
        df[columns_to_impute] = df[columns_to_impute].replace(0, np.nan)
        df[columns_to_impute] = df[columns_to_impute].replace(0, np.nan)
        df.loc[(df['Glucose'] == 0) & (df['SkinThickness'].isnull()), 'Glucose'] = np.nan
        df.loc[(df['Glucose'] == 0) & (df['BloodPressure'].isnull()), 'Glucose'] = np.nan
        df.loc[(df['Glucose'] == 0) & (df['BMI'].isnull()), 'Glucose'] = np.nan
        df.loc[(df['Insulin'] == 0) & (df['SkinThickness'].isnull()), 'Insulin'] = np.nan
        df.loc[(df['Insulin'] == 0) & (df['BloodPressure'].isnull()), 'Insulin'] = np.nan
        df.loc[(df['Insulin'] == 0) & (df['BMI'].isnull()), 'Insulin'] = np.nan
        df['Glucose'] = df['Glucose'].replace(0, np.nan)
        df.loc[(df['Insulin'] == 0) & (df['Glucose'].isnull()), 'Insulin'] = np.nan
        df['Insulin'] = df['Insulin'].replace(0, np.nan)
        return df
    
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        raise