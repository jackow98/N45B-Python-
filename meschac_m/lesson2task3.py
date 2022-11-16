# Mr walker's feedback
# Great start, you just needed an if statement at the end

scot_g_total = 37
scot_games = 15
spain_g_total = 35
spain_games = 14
germany_g_total = 38
germany_games = 15

scot_average = scot_g_total / scot_games
spain_average = spain_g_total / spain_games
germany_average = germany_g_total / germany_games

print("Scotland averaged " + str(scot_average))
print("Spain averaged " + str(spain_average))
print("Germany averaged " + str(germany_average))

# You just needed an if statement at the end
if scot_average > spain_average and scot_average < germany_average:
    print(
        "Scotland's average goals is higher than Spain and less than Germany")
else:
    print("Scotland's average goals is not higher than Spain and less than Germany")
