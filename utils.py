import math
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import log_loss

def train_data(path='data/numerai_training_data.csv'):

    training_data = pd.read_csv(path, header=0)
    features = [f for f in list(training_data) if "feature" in f]

    X = training_data[features]
    Y = training_data["target"]

    return X, Y

def pred_data(path='data/numerai_tournament_data.csv'):
    prediction_data = pd.read_csv(path, header=0)
    features = [f for f in list(prediction_data) if "feature" in f]
    x_prediction = prediction_data[features]
    ids = prediction_data["id"]
    
    return x_prediction, ids

def save_pred(y_prediction, ids, path='predictions.csv'):
    results = y_prediction[:, 1]
    results_df = pd.DataFrame(data={'probability':results})
    joined = pd.DataFrame(ids).join(results_df)
    joined.to_csv(path, index=False)
    
def val_data(path='data/numerai_tournament_data.csv'):
    prediction_data = pd.read_csv(path, header=0)
    validation_data = prediction_data[prediction_data['data_type'] == 'validation']
    features = [f for f in list(validation_data) if "feature" in f]
    x_validation = validation_data[features]
    y_validation = validation_data["target"]
    
    return x_validation, y_validation

def validate(y_true, y_pred, bl=None, inspect=False):
    logloss = log_loss(y_true, y_pred)
    ret = logloss
    if inspect:
        ret = (logloss, -math.log(0.5) - logloss)
        if baseline is not None:
            ret += (bl - logloss,)
    return ret


def baseline(x_train=None, y_train=None, x_val=None, y_val=None):
    if x_train is None or y_train is None:
        x_train, y_train = train_data()
    if x_val is None or y_val is None:
        x_val, y_val = val_data()

    model = linear_model.LogisticRegression(n_jobs=-1)
    model.fit(x_train, y_train)

    y_val_pred = model.predict_proba(x_val)
    logloss = validate(y_val, y_val_pred)
    
    return logloss
