# Mr walker's feedback
# Great start

# Well done, use an integer instead of string
times = [0] * 10

for counter in range(0, 10):
    times[counter] = int(input('Enter swimming time(seconds): '))
    # Make sure you indent so anything below happens within the loop
    # Make sure you use times[counter] to add to correct position in array
    min = times[counter] / 60

    # Remember to round to 1 decimal place
    print('Swimmers time: ', round(min, 1), ' minutes')
