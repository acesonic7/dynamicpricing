def calculate_dynamic_price(vehicle_type, distance, operational_cost_per_km, time_window):
    # Set default adjustments
    vehicle_adjustment = 1  # Default to no adjustment
    time_window_adjustment = 1  # Default to no adjustment

    # Base Price Calculation
    base_price = distance * operational_cost_per_km

    # Vehicle Type Adjustment
    if vehicle_type == "bike":
        vehicle_adjustment = 0.9  # 10% discount for using a bike
    elif vehicle_type == "van":
        vehicle_adjustment = 1.2  # 20% surcharge for using a van

    # Time Window Adjustment
    if time_window == "peak":
        time_window_adjustment = 1.15  # 15% surcharge during peak times
    elif time_window == "off-peak":
        time_window_adjustment = 0.9  # 10% discount during off-peak times

    # Calculating Final Price
    final_price = base_price * vehicle_adjustment * time_window_adjustment
    return final_price
