'''
You live 4 miles form university.The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take?Alternatively, you could run to university. You jog the first mile  at 7mph, then run
the next two at 15mph, before jogging the last at 7mph again.Will this be slower or quicker than the bus?
'''

#For Bus
DistanceInMiles=4
BusSpeedInMiles=25
NumberOfStops=10
TimeStopped=2
TimeTakenByBus= (DistanceInMiles/BusSpeedInMiles)
Hault=(NumberOfStops*TimeStopped)/60
TotalTimeTaken=float(TimeTakenByBus+Hault)
print(f'The time taken by bus is: {TotalTimeTaken} Hours')

#For Jogging
SpeedForFirstMile=7
TimeForFirstMile=1/7
SpeedForNextTwoMiles=15
TimeForNextTwoMiles=2/SpeedForNextTwoMiles
SpeedForLastMile=7
TimeForLastMile=1/7
TotalTime=(TimeForFirstMile+TimeForNextTwoMiles+TimeForLastMile)
print(f'The time taken by jogging is: {TotalTime} Hours')
if TotalTime<TotalTimeTaken:
    print("Jogging is faster")


