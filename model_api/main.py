import joblib
import uvicorn
from fastapi import FastAPI

from models import DeviceInput, PredictionOutput

# Initialize FastAPI
app = FastAPI()

# Load the trained model
model = joblib.load('model.joblib')

@app.post("/predict", response_model=PredictionOutput)
async def predict_device_price(device: DeviceInput):
    device_data = [
        [
            device.battery_power,
            device.four_g,
            device.int_memory,
            device.mobile_wt,
            device.n_cores,
            device.ram/1024,
            device.touch_screen,
            device.px_height*device.px_width,
        ]
    ]
    
    # Get the prediction from the model
    prediction = model.predict(device_data)
    
    # Return the predicted price range
    return PredictionOutput(predicted_price=int(prediction[0]))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)