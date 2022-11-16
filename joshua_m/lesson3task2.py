# Mr walker's feedback
# Good start, see comments below

weight = input('Enter Boxer weight in Kg: ')
pounds = float(weight) * 2.20462

# We need to loop until this condition is met so we need a while loop
while pounds < 100 or pounds > 105:
    weight = int(input(str(pounds) + " pounds is not valid, Re-enter your weight in kg: "))
    pounds = float(weight) * 2.20462
    # Remember to round
    pounds = round(pounds, 1)

print('Boxer is within weight limit.')
