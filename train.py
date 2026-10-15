import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

MODEL_PATH = os.getenv("MODEL_PATH", "/models/model.joblib")

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

modeles = {
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42),
}

scores = {}
for nom, modele in modeles.items():
    modele.fit(X_tr, y_tr)
    scores[nom] = modele.score(X_te, y_te)
    print(f"Accuracy test {nom} : {scores[nom]:.3f}")

meilleur = max(scores, key=scores.get)
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(modeles[meilleur], MODEL_PATH)
print(f"Meilleur modele : {meilleur}, sauvegarde dans {MODEL_PATH}")