# Convert a word to lowercase
def string_to_lowercase(parameter):
    return parameter.strip().lower()



# Check if an input is string or not
def is_estring(parameter):
    return isinstance(parameter, str)


def calculate_calories(body_weight, distance, weight_unit="KG"):
    try:
        
        if not (isinstance(body_weight, (int, float)) and isinstance(distance, (int, float))):
            return TypeError("Body weight and distance must be numbers")
        
        
        # body_weight = float(body_weight)
        # distance = float(distance)
        

        if body_weight < 0 or distance < 0:
            return "Input values should be greater than 0"

        if weight_unit == "KG":
            base_kcal = 0.97
            total_calories = distance * (base_kcal * body_weight)
            return round(total_calories, 2)

        elif weight_unit == "LB":
            
            body_weight_kg = body_weight * 0.45359237
            base_kcal = 0.97
            total_calories = distance * (base_kcal * body_weight_kg)
            return round(total_calories, 2)

        else:
            return "Invalid weight unit. Please specify 'KG' or 'LB'."

    except ValueError as value_err:
        return f"{value_err} / Please enter valid arguments"


def kilograms_lost(kcal):
    """
    This function calculates how many days are necessary to
    lose 1 kg of body fat, based on the amount of calories burned
    Parameter: kcal represents the calories burned in physical activity
    """
    try:
        kcal_float = float(kcal)
        if kcal_float <= 0:
            return "Calories burned must be greater than 0"

        kg_in_kcal = 7000
        total_days = kg_in_kcal / kcal_float
        return round(total_days)

    except (ValueError, TypeError) as err:
        return "Please, enter a valid input"
