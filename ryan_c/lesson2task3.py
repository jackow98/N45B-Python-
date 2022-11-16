# Mr walker's feedback
# Good start, few comments below

scotlandgoals = 37
scotlandgames = 15
# Average goals is total goals divided by total games, I have corrected below
scotlandaverage = scotlandgoals / scotlandgames

spaingoals = 35
spaingames = 14
spainaverage = spaingoals / spaingames

germanygoals = 38
germanygames = 15
germanyaverage = germanygoals / germanygames

# Be careful with printing, I would use more print statements that are smaller
# Having big print statements like this is difficult to read
print('Scotland stat: ' + 'total goals, ' + str(scotlandgoals) + 'Total games,' + str(scotlandgames) + 'goal average,' + str(scotlandaverage))
print('Spain stat: ' + 'total goals, ' + str(spaingoals) + 'Total games,' + str(spaingames) + 'goal average,' + str(spainaverage))
print('Germany stat: ' + 'total goals, ' + str(germanygoals) + 'Total games,' + str(germanygames) + 'goal average,' + str(germanyaverage))

# You just needed an if statement at the end
if scotlandaverage > spainaverage and scotlandaverage < germanyaverage:
    print(
        "Scotland's average goals is higher than Spain and less than Germany")
else:
    print("Scotland's average goals is not higher than Spain and less than Germany")
