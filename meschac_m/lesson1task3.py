# Mr walker's feedback
# Good work, just a few things to be careful of

qualifier_games = 7
qualifier_goals = 15
euro_games = 8
euro_goals = 22

# You had your average calculations round the wrong way
# Remember average = total/goals
average_qualifiers = qualifier_goals / qualifier_games
average_euros = euro_goals / euro_games

# Just be careful with spacing when concatenating
# Also, use multiple print statements so code is easier to read
print("In the qualifiers they averaged " + str(average_qualifiers) + " goals.")
print("In the Euros they averaged " + str(average_euros) + " goals.")

# To calculate the total average, you could either:
totalAverage1 = (average_qualifiers + average_euros) / 2
totalAverage2 = (qualifier_goals + euro_goals) / (qualifier_games + euro_games)
print(totalAverage1)
print(totalAverage2)