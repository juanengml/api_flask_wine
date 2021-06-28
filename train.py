import numpy as np
import pandas as pd

import joblib

from sklearn.ensemble import RandomForestClassifier
from console_logging.console import Console
console = Console()

def main():
    df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
    df['species'] = df['species'].map({'setosa': 0, 'virginica': 1, 'versicolor': 2})
    X_train = df.drop('species', axis = 1)
    y_train = df['species']
    rf_classifier = RandomForestClassifier()
    console.info("TRAIN MODEL...")
    rf_classifier.fit(X_train, y_train)
    console.success("DUMP MODEL... ")
    joblib.dump(rf_classifier, "model.pkl")

if __name__ == "__main__":
    main()    