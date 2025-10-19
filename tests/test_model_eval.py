import joblib
import pandas as pd
from sklearn import metrics

def test_model_accuracy():
    # Load data and model from local DVC workspace
    eval_df = pd.read_csv("data/v2/data_augmented.csv")
    X_eval = eval_df[['sepal_length','sepal_width','petal_length','petal_width']]
    y_true = eval_df['species']
    model = joblib.load("artifacts/latest/iris_model.joblib")  # Or your timestamped folder
    preds = model.predict(X_eval)

    acc = metrics.accuracy_score(y_true, preds)
    assert acc > 0.9, f"Model accuracy below threshold: {acc:.3f}"
