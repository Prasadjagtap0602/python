import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

data = {
    "Time_Spent": np.random.randint(1, 100, 500),
    "Pages_Visited": np.random.randint(1, 10, 500),
    "Country": np.random.choice(["USA", "India", "UK"], 500),
    "Returning_User": np.random.choice(["Yes", "No"], 500),
    "Purchase": np.random.choice([0, 1], 500, p=[0.6, 0.4])
}

df = pd.DataFrame(data)

X = df[["Time_Spent", "Pages_Visited", "Country", "Returning_User"]]
y = df["Purchase"]

categorical_cols = ["Country", "Returning_User"]
numeric_cols = ["Time_Spent", "Pages_Visited"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=200, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

def predict_purchase(time_spent, pages_visited, country, returning_user):
    input_data = pd.DataFrame([{
        "Time_Spent": time_spent,
        "Pages_Visited": pages_visited,
        "Country": country,
        "Returning_User": returning_user
    }])
    prob = model.predict_proba(input_data)[0][1]
    pred = "Yes" if prob >= 0.5 else "No"
    print(f"Purchase Prediction: {pred} ({prob*100:.2f}% likelihood)")
    return pred, prob

predict_purchase(45, 7, "USA", "Yes")

