def calculate_final_price(delivery_option: dict) -> float:
    # Placeholder for a more complex pricing logic
    base_price = 10  # Base price
    price_modifier = 1  # Modifier that could change based on conditions

    # Example logic: Adjust price_modifier based on delivery type
    if delivery_option.get("type") == "express":
        price_modifier = 1.5
    elif delivery_option.get("type") == "eco":
        price_modifier = 0.8

    # Calculate final price
    final_price = base_price * price_modifier
    return final_price
