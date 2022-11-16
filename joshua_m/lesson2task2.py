# Mr walker's feedback
# Great work, you just rounded wrong and got confused with if statements

# Remember you can use round()
weight = round(104.4991, 1)

if weight > 105:
    print('Boxer is above upper limit.')
# You should use elif here as you only do this if the first statement is false
elif weight < 105 and weight > 100:
    # You should say boxer is within limit here
    print('Boxer is within limits.')
else:
    # Remember to print
    print('Boxer is below lower limit.')