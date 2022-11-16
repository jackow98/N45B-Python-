# Mr walker's feedback
# Good start, see comments below

# Be careful with variable naming
# boxerkg should be boxerKg or boxer_kg
boxerkg = int(input("What is your weight in kg?"))

# You don't need brackets here
boxerpounds = boxerkg * 2.205

# We need to loop until this condition is met so we need a while loop
while boxerpounds < 100 or boxerpounds > 105:
    boxerkg = int(input(str(boxerpounds) + " pounds is not valid, Re-enter your weight in kg: "))
    # Remember to round
    boxerpounds = round(boxerkg * 2.205,1)

# If we break out the while loop, it is because the condition has been met
print("You are successfully in the weight limit!")
