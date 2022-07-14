import pickle 
import pandas as pd
from sklearn.preprocessing import RobustScaler


def get_prediction(X, model_path, sample_df_path):
    
    # Replicate feature engineering 
    cat_cols = ['workclass', 'education', 'marital-status', 'occupation',
                'relationship', 'race', 'sex', 'native-country']
    X_one_hot = pd.get_dummies(X, columns = cat_cols)
    #RobustScaler().fit(X_one_hot)
    
    # load sample df (empty) with the same columns as the original model when was trained
    new_obs = pickle.load(open(sample_df_path, 'rb'))
    print("---new_obs--:")
    print(new_obs)
    
    # fill matching columns
    print('--X_one_hot.columns--')
    print(X_one_hot.columns)
    for col in X_one_hot.columns : 
        print("---> Current column is %s:"%(col))
        print("-----> new_obs[%s]=%s"%(col, str(new_obs[col])))
        print("-----> X_one_hot[%s]=%s"%(col, str( X_one_hot[col])))
        new_obs[col] = X_one_hot[col].tolist()
    
    # load trained model
    loaded_model = pickle.load(open(model_path, 'rb'))
    print("---------------------new_obs-------------------")
    print(new_obs)
    
    print("---------------------loaded_model-------------------")
    print(loaded_model)
    preds = loaded_model.predict(new_obs)
    return preds