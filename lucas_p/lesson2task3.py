# Mr walker's feedback
# Great start, just be careful with variable naming
# scotlandgames should be scotlandGames or scotland_games

scotlandtotalgoals = 37
scotlandgames = 15
scotlandaverage = scotlandtotalgoals/scotlandgames
print(scotlandaverage)

spaintotalgoals = 35
spaingames=14
spainaverage = spaintotalgoals / spaingames
print(spainaverage)

germanygoals = 38
germanygames = 15
germanyaverage = germanygoals/germanygames
print(germanyaverage)

# You just needed an if statement at the end
if scotlandaverage > spainaverage and scotlandaverage < germanyaverage:
    print(
        "Scotland's average goals is higher than Spain and less than Germany")
else:
    print("Scotland's average goals is not higher than Spain and less than Germany")
