# Mr walker's feedback
# Great work!

total_scot_goals = 37
scot_games = 15

total_spain_goals = 35
spain_games = 14

total_germ_goals = 38
germ_games = 15

scot_average = total_scot_goals / scot_games
spain_average = total_spain_goals / spain_games
germ_average = total_germ_goals / germ_games

scot_average = round(scot_average, 2)
spain_average = round(spain_average, 2)
germ_average = round(germ_average, 2)

if scot_average > spain_average:
    print("Scotland had a higher average of goals per game of", scot_average,
          "while Spain had", spain_average)

else:
    print("Spain had a higher average of goals per game of", spain_average,
          "while Scotland had", scot_average)

if scot_average < germ_average:
    print("Scotland had a lesser average of goals per game of", scot_average,
          "while Germany had", germ_average)

else:
    print("Germany had a lesser average of goals per game of", germ_average,
          "while Scotland had", scot_average)