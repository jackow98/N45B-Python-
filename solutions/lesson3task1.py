for i in range(1, 11):
    swimmerTimeSec = input("Please enter swimmer " + str(i) + "’s time in seconds:")
    swimmerTimeMin = int(swimmerTimeSec) / 60
    swimmerTimeMin = round(swimmerTimeMin, 1)

    print("Swimmer " + str(i) + "'s time was " + str(swimmerTimeMin) + " mins")