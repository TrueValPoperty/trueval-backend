# Predict Endpoint Patch

## What's Included

- `routes/predict.py`: A new POST `/predict` endpoint that loads a trained model and returns price predictions.
- `model/`: Create this folder in your backend and drop your trained `model.pkl` here.

## Usage

1. Add this to your Flask app:
```python
from routes.predict import predict_price
app.add_url_rule("/predict", view_func=predict_price, methods=["POST"])
```

2. Restart your app after placing `model.pkl` in the `model/` folder.
