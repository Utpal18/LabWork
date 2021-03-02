''' Given the N- Number of minutes that is passed since midnight- How many hours and minutes are displayed on 24 h
digital clock.'''

minutes=int(input("Enter time in minutes: "))
hours= minutes//60
min=minutes%60
print(f'The time is: {hours} hr {min} minutes')

