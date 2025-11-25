# --- Manual Naive Bayes for Mushroom Dataset (Cleaned & Improved Version) ---
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("==============================================")
print("🍄 MUSHROOM DATASET – MANUAL NAIVE BAYES MODEL")
print("==============================================\n")

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv(r"D:\python\AI-Assignment\mushrooms.csv")

print("🔹 Dataset Shape:", df.shape)
print("🔹 Columns:", df.columns.tolist())
print("\n🔹 First 5 Rows:\n", df.head())

print("\n🔹 Class Distribution:\n", df['class'].value_counts())

# -----------------------------
# 2. Encode class as numeric
# -----------------------------
df['class'] = df['class'].map({'e': 0, 'p': 1})   # edible=0, poisonous=1

# -----------------------------
# 3. Train–Test Split
# -----------------------------
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

X_train = train_df.drop('class', axis=1)
y_train = train_df['class']

X_test = test_df.drop('class', axis=1)
y_test = test_df['class']

# -----------------------------
# 4. Calculate Priors
# -----------------------------
P_poison = np.mean(y_train)
P_edible = 1 - P_poison

print("\n🔹 Prior Probabilities:")
print(f"P(Poisonous=1): {P_poison*100:.2f}%")
print(f"P(Edible=0): {P_edible*100:.2f}%")

# -----------------------------
# 5. Conditional Probabilities (Laplace Smoothing Included)
# -----------------------------
def calculate_conditional_probabilities(X, y):
    cond_probs = {}

    for col in X.columns:
        cond_probs[col] = {}
        unique_vals = X[col].unique()

        for val in unique_vals:
            # Laplace smoothing: +1 numerator, +K denominator
            p_val_given_edible = (
                ((X[col] == val) & (y == 0)).sum() + 1
            ) / ((y == 0).sum() + len(unique_vals))

            p_val_given_poison = (
                ((X[col] == val) & (y == 1)).sum() + 1
            ) / ((y == 1).sum() + len(unique_vals))

            cond_probs[col][val] = {0: p_val_given_edible, 1: p_val_given_poison}

    return cond_probs


conditional_probs = calculate_conditional_probabilities(X_train, y_train)

# -----------------------------
# 6. Manual Prediction Function
# -----------------------------
def predict_with_probs(sample):
    probs = {}

    for cls in [0, 1]:  # edible=0, poisonous=1
        prob = P_edible if cls == 0 else P_poison
        
        for feature in X_train.columns:
            value = sample[feature]

            # If new unseen value appears → apply smoothing
            if value in conditional_probs[feature]:
                prob *= conditional_probs[feature][value][cls]
            else:
                # Stronger Laplace smoothing for completely unseen cases
                prob *= 1e-6

        probs[cls] = prob

    # Normalize to probabilities (percentage)
    total = probs[0] + probs[1]
    probs_normalized = {cls: (probs[cls]/total)*100 for cls in probs}

    predicted_class = 0 if probs[0] > probs[1] else 1
    return probs_normalized, predicted_class


# -----------------------------
# 7. Test on Random Samples
# -----------------------------
print("\n🔍 Predictions for 5 Random Test Samples:\n")

sample_idx = np.random.choice(len(X_test), 5, replace=False)
sample_data = X_test.iloc[sample_idx]

for i, (idx, row) in enumerate(sample_data.iterrows()):
    probs, pred = predict_with_probs(row)

    actual = "Poisonous" if y_test.loc[idx] == 1 else "Edible"
    predicted = "Poisonous" if pred == 1 else "Edible"

    print(f"===============================")
    print(f"🍄 Sample {i+1}")
    print("--- Features ---")
    for f, v in row.items():
        print(f"  {f}: {v}")
    print(f"True Class: {actual}")
    print(f"Predicted Class: {predicted}")
    print(f"P(Edible=0): {probs[0]:.2f}%")
    print(f"P(Poisonous=1): {probs[1]:.2f}%")
    print("===============================\n")

# -----------------------------
# 8. Final Evaluation
# -----------------------------
preds = []
for _, row in X_test.iterrows():
    _, p = predict_with_probs(row)
    preds.append(p)

acc = accuracy_score(y_test, preds) * 100
cm = confusion_matrix(y_test, preds)
report = classification_report(y_test, preds)

print(f"\n✅ Overall Accuracy: {acc:.2f}%")
print("\n🔹 Confusion Matrix:\n", cm)
print("\n🔹 Classification Report:\n", report)
