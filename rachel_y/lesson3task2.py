# Mr walker's feedback
# Great work

# For this program, we want the user to input the weighr
boxerWeight = input("Please enter boxer weight in KG:")

upperLimit = 105
lowerLimit = 100

# Remember to convert to pounds
boxerWeightPounds = float(boxerWeight) * 2.2
boxerWeightPounds = round(boxerWeightPounds, 1)

print("The boxer weight is", str(boxerWeightPounds) + " pounds")

# We do not need an if statement
# We need to loop until this condition is met so we need a while loop
while boxerWeightPounds > 105 or boxerWeightPounds < 100:
    # We need to ask user to re-enter every time it is wrong
    weight = int(input(str(boxerWeightPounds) + " pounds is not valid, Re-enter your weight in kg: "))
    boxerWeightPounds = float(weight) * 2.20462
    # Remember to round
    boxerWeightPounds = round(boxerWeightPounds, 1)

print('Boxer is within weight limit.')