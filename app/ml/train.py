from app import create_app
from app.ml.data import TrainingData
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

app = create_app()

with app.app_context():
    print("Loading data...")

    df = TrainingData.load()

    # Convert to datetime
    df["date"] = df["date"].astype("datetime64[ns]")

    # Time features
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.weekday

    X = df[[
        "product_id",
        "day",
        "month",
        "weekday"
    ]]

    y = df["quantity"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,
        test_size=0.2,
        random_state=42
    )

    print("Training model.....")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test, predictions
    )

    print()
    print("="*40)
    print("Training Complete")
    print("="*40)
    print(f"MAE : {mae:.2f}")

    joblib.dump(
        model,
        "app/ml/model.pkl"
    )

    print("Model saved successfully.")

    print(df.head())

    print()

    print(df.dtypes)
