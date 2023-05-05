from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import datetime

from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import joblib
import datetime


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier(max_depth=10, random_state=42, n_estimators=75)
        self.model.fit(features, target)
        self.timestamp = datetime.datetime.now()

    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        confidence, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(confidence)

    def save(self, filepath):
        return joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f"Base Model: {self.name}<br>Timestamp: {self.timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}"