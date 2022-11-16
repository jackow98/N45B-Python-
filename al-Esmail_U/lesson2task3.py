# Mr walker's feedback
# Great work

scgoals =37
scgames =15
spgoals =35
spgames =14
gegoals =38
gegames =15

# You don't need brackets here
scaverage = scgoals/scgames
spaverage = spgoals/spgames
geaverage = gegoals/gegames

# Good work here, you could simplify to
# ---START----
if  scaverage > spaverage  and scaverage < geaverage:
    print(
        "Scotland's average goals is higher than Spain and less than Germany")
else:
    print("Scotland's average goals is not higher than Spain and less than Germany")
# ---END---

if scaverage > spaverage and scaverage < geaverage:
    print("Scotland had more average goals than Spain but not Germany")

elif scaverage < spaverage and scaverage > geaverage:
    print("Scotland had more average goals than Germany but not Spain")

elif scaverage > spaverage and scaverage > geaverage:
    print("Scotland had more average goals than Spain and Germany")

elif scaverage < spaverage and scaverage < geaverage:
    print("Scotland has less average goals than Spain and Germany")

else:
    print("Something went wrong. Please try again.")

