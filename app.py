from flask import Flask, request, jsonify

from pricingfunction import calculate_dynamic_price

app = Flask(__name__)

@app.route('/api/calculate-price', methods=['POST'])
def calculate_price():
    # Parse the incoming JSON data
    data = request.get_json()

    # Extract variables from the parsed JSON
    vehicle_type = data['vehicle_type']
    distance = data['distance']
    operational_cost_per_km = data['operational_cost_per_km']
    time_window = data['time_window']

    # Call your dynamic pricing function
    price = calculate_dynamic_price(vehicle_type, distance, operational_cost_per_km, time_window)

    # Return the price in the response
    return jsonify({"calculated_price": price})

if __name__ == '__main__':
    app.run(debug=True)
