print('       METRO NAVIGATOR            ')
from tabulate import tabulate
import pandas as pd

# Metro station data
data = [
    [1, 'RAIDURG'], [2, 'HITEC CITY'], [3, 'DURGAM CHERUVU'], [4, 'MADHAPUR'],
    [5, 'PEDDAMMA GUDI'], [6, 'JUBILEE HILLS CHECKPOST'], [7, 'ROAD NO.5 JUBILEE HILLS'],
    [8, 'YUSUFGUDA'], [9, 'MADHURA NAGAR'], [10, 'AMEERPET'], [11, 'BEGUMPET'],
    [12, 'PRAKASH NAGAR'], [13, 'RASOOLPURA'], [14, 'PARADISE'], [15, 'PARADE GROUND'],
    [16, 'SECUNDERABAD EAST'], [17, 'METTUGUDA'], [18, 'TARNAKA'], [19, 'HABSIGUDA'],
    [20, 'NGRI'], [21, 'STADIUM'], [22, 'UPPAL'], [23, 'NAAGOL']
]

print(tabulate(data, headers=["STATION NO.", 'STATION NAME']))

# Metro station distances, times, and costs
distance = [1.5, 0.8, 6.9, 16.9, 0.9, 0.6, 13.4, 1.4, 0.7, 1.6, 1.4, 1.1, 1, 1.2, 1.6, 1.9, 1.3, 1.6, 0.9, 1.2, 1.1, 1]
time = [3, 1, 2, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2, 2]
cost = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# User input for station numbers
try:
    si = int(input('Enter the station number you are at (si): '))
    sf = int(input('Enter the station number you want to go to (sf): '))

    # Validate inputs
    if si < 1 or si > len(data) or sf < 1 or sf > len(data):
        print('INVALID STATION NUMBER! Please enter a valid station number.')
    else:
        # Calculate distance, time, and cost
        dis, tim, cos = 0, 0, 0
        if si < sf:
            for i in range(si - 1, sf - 1):
                dis += distance[i]
                tim += time[i]
                cos += cost[i]
        elif si > sf:
            for i in range(si - 2, sf - 2, -1):  # Reverse traversal
                dis += distance[i]
                tim += time[i]
                cos += cost[i]

        # Display results
        result = {'DISTANCE (km)': [dis], 'TIME (min)': [tim], 'COST (₹)': [cos]}
        df = pd.DataFrame(result)
        print("\nSummary of your journey:")
        print(df.to_string(index=False))
except ValueError:
    print("Please enter valid numeric station numbers!")
