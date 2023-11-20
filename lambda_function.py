import os
import boto3
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

s3 = boto3.client('s3')

def load_csv_from_s3(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    return df

def load_pkl_from_s3(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    model = pickle.load(obj['Body'])
    return model

def calculate_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def lambda_handler(event, context):
    # S3イベントから取得した情報
    bucket = event['Records'][0]['s3']['bucket']['name']
    x_test_key = event['Records'][0]['s3']['object']['key']
    model_key = "random_forest_model.pkl"  # 学習済みモデルのファイル名

    # S3からCSVデータと学習済みモデルをロード
    x_test = load_csv_from_s3(bucket, x_test_key)
    model = load_pkl_from_s3(bucket, model_key)

    # データの前処理（必要に応じて追加）

    # 予測
    X_test = np.array(x_test.drop(['target'], axis=1))
    y_test = np.array(x_test['target'])
    y_pred = model.predict(X_test)

    # 精度の計算
    accuracy = calculate_accuracy(y_test, y_pred)

    # 結果をログに出力
    print(f'Loaded Model Accuracy: {accuracy}')

    # Lambda関数のレスポンスとしても返す場合は以下のように記述
    return {
        'statusCode': 200,
        'body': f'Loaded Model Accuracy: {accuracy}'
    }
