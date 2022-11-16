# Mr walker's feedback
# Good start, you just need a few more lines

total = 104.4991
roundedWeight = round(total, 1)
print(roundedWeight)

upperLim = 105.0
lowerLim = 100.0

# You need an if statement to do the check
if roundedWeight > lowerLim and roundedWeight < upperLim:
    print("Boxer qualifies")
else:
    print("Boxer does not qualify")
