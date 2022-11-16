# Mr walker's feedback
# You have overcomplicated this!

# This is all the code you need
# ----START----
ukTime = 50.32
usaTime = 49.32

if ukTime <= 50 or usaTime <= 50:
    print("Swimmer qualifies")
else:
    print("Swimmer does not qualify")
# ----END----


# You don't need the variable total
total = 0
uk = 50.32
us = 49.32
# This should be <=
if total + uk < 50:
    print('Team UK is through.')
else:
    print('Team UK is out.')

if total + us < 50:
    print('Team US is through.')
else:
    print('Team US is out.')

