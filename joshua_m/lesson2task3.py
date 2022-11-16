# Mr walker's feedback
# Great work, have a look below at alternative to nested if statements

scotlandGoals = 37
scotlandGames = 15
scotlandAverage = scotlandGoals / scotlandGames

spainGoals = 35
spainGames = 14
spainAverage = spainGoals / spainGames

germanyGoals = 38
germanyGames = 15
germanyAverage = germanyGoals / germanyGames

# You had two if statements nested, you can put this all-in-one line using and
if germanyAverage > scotlandAverage and scotlandAverage > spainAverage:
    print('Scotland has more average goals than Spain but less than Germany.')

if germanyAverage < scotlandAverage:
    print('Germany had a smaller average goals ration than Scotland')
# You should use elif here as you only do this if the first statement is false
elif spainAverage > scotlandAverage:
    print('Spain had a higher average goals ratio than Scotland')
