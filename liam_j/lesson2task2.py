# Mr walker's feedback
# Great work, just make sure print statements are clearer

boxerWeight = round(104.4991, 1)

if boxerWeight > 105.0:
    print("Boxer is too heavy")
elif boxerWeight < 105.0 and boxerWeight > 100.0:
    print("Boxer qualifies")
# If you are printing when boxer is too heavy, I would have a third branch for too light
else:
    print("Boxer is too light")
