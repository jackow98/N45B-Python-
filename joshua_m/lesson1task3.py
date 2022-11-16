# Mr walker's feedback
# Great work! Be careful with your maths

# I would suggest using more readable variable names than qGames
qGames = 7
qGoals = 15
qAverage = qGoals / qGames

eGames = 8
eGoals = 22
eAverage = eGoals / eGames

# If you are going to calculate the averages separately,
# you would need to calculate the average of the averages so either:
totalAverage1 = (qAverage + eAverage) / 2
totalAverage2 = (qGoals + eGoals) / (qGames + eGames)

print('Average goals for Scotland in qualifiers and Euros were ', round(totalAverage1))
print('Average goals for Scotland in qualifiers and Euros were ', round(totalAverage2))
