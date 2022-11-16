# Mr walker's feedback
# Good work, just be careful with variable naming

boxersKg = float(input("your weight in kg?"))
boxerPounds = (boxersKg *2.205)
# You can use the same variable and overwrite
boxerPounds = round(boxerPounds,1)
print(boxerPounds)

# Have an else statement to make sure something always prints
if boxerPounds <100 and boxerPounds >105:
    print("Boxer is eligible")
else:
    print("Boxer is not eligible")

