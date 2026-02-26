import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# ✅ Load Dataset
df = pd.read_csv("dataset_full.csv")
df = df.dropna()

# ✅ Separate features and label
X = df.drop(columns=["phishing"])
y = df["phishing"]

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Evaluation
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save Model
joblib.dump(model, "phishing_model_dataset_full.pkl")
print("✅ Model saved as phishing_model_dataset_full.pkl")
