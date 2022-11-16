# Mr walker's feedback
# Good start, you just need a few more lines

upperLimit = 105
lowerLimit = 100

# Remember to create a variable here
# Also, use the 1 to round to 1 decimal place
roundedWeight = round(104.4991, 1)
print(roundedWeight)

if roundedWeight > lowerLimit and roundedWeight < upperLimit:
    print("Boxer qualifies")
else:
    print("Boxer does not qualify")
