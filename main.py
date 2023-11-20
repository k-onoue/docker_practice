import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

data_path = "./test_data.csv"
model_path = './random_forest_model.pkl'

def main():
    # データの読み込み
    test_data = pd.read_csv(data_path)

    X_test = np.array(test_data.drop(['target'], axis=1))
    y_test = np.array(test_data['target'])

    # モデルの読み込み
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # モデルの評価
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    # print(f'Loaded Model Accuracy: {accuracy}')
    
    return {
        "Accuracy": accuracy
    }



if __name__ == "__main__":
    main()