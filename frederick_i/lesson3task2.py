# Mr walker's feedback
# Good start, see solution below

BoxerWeight = input()
print ("Please enter your weight in kg")

# ---CORRECT SOLUTION START----
boxerWeightKg = input("Please enter boxer weight in KG:")

boxerWeightPounds = float(boxerWeightKg) * 2.2
boxerWeightPounds = round(boxerWeightPounds, 1)

while boxerWeightPounds > 105 or boxerWeightPounds < 100:
    boxerWeightKg = input(str(boxerWeightPounds) + " pounds is not valid, try again:")

    boxerWeightPounds = float(boxerWeightKg) * 2.2
    boxerWeightPounds = round(boxerWeightPounds, 1)

print("Weight of " + str(boxerWeightPounds) + " pounds is valid, boxer is eligible")
# ---CORRECT SOLUTION END----
