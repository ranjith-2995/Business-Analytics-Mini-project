# Student Score Prediction using Random Forest Regressor
# ------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1️⃣ Load or create dataset
data = {
    'study_hours': [2, 3, 4, 5, 1, 6, 7, 8, 9, 10, 5, 6, 3, 2, 8],
    'attendance': [80, 85, 90, 95, 60, 98, 99, 100, 95, 97, 89, 92, 78, 65, 96],
    'past_score': [55, 60, 65, 70, 50, 80, 85, 88, 90, 95, 72, 76, 60, 58, 91],
    'final_score': [60, 65, 70, 75, 55, 82, 87, 90, 92, 95, 78, 80, 66, 60, 93]
}

df = pd.DataFrame(data)
print("Sample Dataset:\n", df.head())

# 2️⃣ Define features and target
X = df[['study_hours', 'attendance', 'past_score']]
y = df['final_score']

# 3️⃣ Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Make predictions
y_pred = model.predict(X_test)

# 6️⃣ Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n Model Evaluation:")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Root Mean Squared Error (RMSE):", round(rmse, 2))
print("R² Score:", round(r2, 3))

# 7️⃣ Display Feature Importance
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print("\n Feature Importance:\n", feature_importance)

# Plot feature importance
plt.figure(figsize=(6,4))
feature_importance.sort_values().plot(kind='barh', color='skyblue')
plt.title("Feature Importance in Student Score Prediction")
plt.xlabel("Importance")
plt.ylabel("Features")
plt.show()

# 8️⃣ Predict for a new student
new_student = pd.DataFrame({
    'study_hours': [6],
    'attendance': [92],
    'past_score': [78]
})

predicted_score = model.predict(new_student)[0]
print(f"\n Predicted Final Score for new student: {predicted_score:.2f}")
