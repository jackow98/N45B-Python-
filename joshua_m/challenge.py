# Mr walker's feedback
# Really greet work! Well done going above and beyond to complete

import time

# You don't need team1, team2 etc., you can use an array
# Use an integer to initialise
teamTotals = [0] * 4

# I would recommend making this clearer as I am unsure what this means
print('W = 3  D = 1  L = 0')
time.sleep(1)

for counter in range(4):
    teamTotals[0] += int(input('how many points did team 1 get? '))
    teamTotals[1] += int(input('how many points did team 2 get? '))
    teamTotals[2] += int(input('how many points did team 3 get? '))
    teamTotals[3] += int(input('how many points did team 4 get? '))

    # Be careful below, you were calculating total round score, not total team score, I have fixed above
    time.sleep(1)
    print('-----------------------------------------------------------------------------------')

# The code below wasn't working as you need to specify team for every comparison
# I have shown you a simpler method below

winningTeam = 0
totalPoints = teamTotals[0]

for team in range(1, 4):
    totalPoints = totalPoints + teamTotals[team]
    if teamTotals[team] > teamTotals[winningTeam]:
        winningTeam = team

print("Team " + str(winningTeam+1) + " wins with " + str(teamTotals[winningTeam]) + " points")
print('Overall points were', str(totalPoints))

# What did you mean by length of characters? 'length of characters would be ', len(teamTotals)
