# Mr walker's feedback
# Good start, see notes below

swimTime = [0] * 10
minutes = [0] * 10

# Make sure everything you want to happen 10 times is within the loop
for counter in range(10):
    print("What is your swimming time?(only in seconds)")
    swimTime[counter] = int(input())
    minutes[counter] = round(swimTime[counter] / 60, 1)

    # Instead of having two loops, you could print here in the first loop
    print("Swimmer", str(counter + 1), "swam for", minutes[counter], "minutes.")