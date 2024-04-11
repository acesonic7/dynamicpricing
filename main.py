from fastapi import FastAPI
from pricingfunction import calculate_final_price  # Import the calculation function

app = FastAPI()

@app.post("/calculate-price/")
def calculate_price(delivery_option: dict):
    # Use the imported function to calculate the price
    final_price = calculate_final_price(delivery_option)
    return {"final_price": final_price}
