import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
import joblib, os, datetime
from google.cloud import storage

def train_data(dataset):
    data = pd.read_csv(dataset)
    print(data.head(5))
    
    train, test = train_test_split(data, test_size = 0.4, stratify = data['species'], random_state = 42)
    X_train = train[['sepal_length','sepal_width','petal_length','petal_width']]
    y_train = train.species
    X_test = test[['sepal_length','sepal_width','petal_length','petal_width']]
    y_test = test.species
    
    mod_dt = DecisionTreeClassifier(max_depth = 3, random_state = 1)
    mod_dt.fit(X_train,y_train)
    prediction=mod_dt.predict(X_test)
    print('\nThe accuracy of the Decision Tree is',"{:.3f}".format(metrics.accuracy_score(prediction,y_test)))
    
    return mod_dt

def store_to_gcs(model):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = f"{MODEL_ARTIFACT_DIR}/artifacts/{timestamp}-iris"
    os.makedirs(output_dir, exist_ok=True)

    # Save model
    joblib.dump(mod_dt, f"{output_dir}/iris_model.joblib")

    # Save metrics
    with open(f"{output_dir}/metrics.txt", "w") as f:
        f.write(f"accuracy: {metrics.accuracy_score(prediction, y_test):.3f}\n")

    # Upload to GCS
    client = storage.Client()
    bucket = client.bucket(BUCKET_URI.split('gs://')[1])
    for file in os.listdir(output_dir):
        blob = bucket.blob(f"{output_dir}/{file}")
        blob.upload_from_filename(f"{output_dir}/{file}")
        
def download_model(bucket_name, model_path, local_file="iris_model.joblib"):
    client = storage.Client()
    blob = client.bucket(bucket_name).blob(model_path)
    blob.download_to_filename(local_file)
    return joblib.load(local_file)

def get_inference(data, model_artifact):
    # Load evaluation data - for data v1
    eval_df = pd.read_csv(data)  # use test set
    X_eval = eval_df[['sepal_length','sepal_width','petal_length','petal_width']]
    
    # Load model from GCS and predict
    model = download_model(BUCKET_NAME, model_artifact)
    preds = model.predict(X_eval)
    eval_df['predictions'] = preds
    print(eval_df.head())
    
    print('\nAccuracy:', "{:.3f}".format(metrics.accuracy_score(eval_df['predictions'], eval_df['species'])))
    
