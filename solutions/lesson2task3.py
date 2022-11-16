scotGoals = 37
scotGames = 15
spainGoals = 35
spainGames = 14
germGoals = 38
germGames = 15

avgScot = scotGoals / scotGames
avgSpain = spainGoals / spainGames
avgGerm = germGames / germGames

print("Scotland had " + str(avgScot) + " average goals")
print("Spain had " + str(avgSpain) + " average goals")
print("Germany had " + str(avgGerm) + " average goals")

if avgScot > avgSpain and avgScot < avgGerm:
    print(
        "Scotland's average goals is higher than Spain and less than Germany")
else:
    print("Scotland's average goals is not higher than Spain and less than Germany")
