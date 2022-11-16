# Mr walker's feedback
# Great work, just a few notes

swimmerTimes = 0
for counter in range(10):
    # Make sure you indent so anything below happens within the loop
    Time = input("what is the time for Swimmer " + str(counter +1))
    # You missed some brackets, break this up into two statements to make it easier like this:
    roundedTime = round(int(Time) / 60, 1)
    print(roundedTime)