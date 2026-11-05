def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("BMI Calculator")

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

if weight <= 0 or height_cm <= 0:
    print("Weight and height must be greater than zero.")
else:
    bmi = calculate_bmi(weight, height_cm / 100)
    print(f"Your BMI is {bmi:.1f}")
    print(f"Category: {get_category(bmi)}")