import matplotlib.pyplot as plt

import numpy as np
import csv

courselength = 1350
filename = 'E:/project/buggydata/1RaceEntries - cmubuggy_table_entry (1).csv'
orgdict = {
        'PKA' : (0,0,0),
        'SDC' : (1,0,0),
        'CIA' : (1,1,0),
        'FRI' : (0,0,1),
        'SN' : (0,1,0),
        'SPI' : (1,0,1),
        'SEP' : (0,1,1),
        'APX' : (1,.5,0),
        'KDR' : (0,1,.5),
        'ATO' : (.5,1,0),
        'BTP' : (.5,0,1),
        'PKT' : (1,0,.5),
        'DTD' : (.25,0,.5),
        'AEP' : (0,0,.75)}
teamdict = {
            'A' : float(100),
            'B' : float(30),
            'C' : float(20),
            'D' : float(10)}
with open(filename) as csvfile:
        readCSV = csv.DictReader(csvfile)
        speedseries = []
        timeseries = []
        classseries = []
        orgcolorseries = []
        orgnameseries = []
        teamseries = []
        
        for row in readCSV:
            
            s = ', '
            if float(row['Prelim']) == 0:
                continue
            color = (0 ,1 ,0)
            orgcolor = (1,0,0)
            if row['Class'] == 'M':
                color = (1, 0 , 0)
    
            
                
            
            timeseries.append([row['Year'], row['Prelim']])
            speedseries.append([row['Year'], courselength/float(row['Prelim'])])
            classseries.append(color)
            if row['orgid'] in orgdict:
                color = orgdict[row['orgid']]
            else:
                color = (.25, .25, .25)    
            orgcolorseries.append(color)
            teamseries.append(teamdict[row['Team']])
            orgnameseries.append(row['orgid'])


timeseries = np.array(timeseries, dtype=float)
speedseries = np.array(speedseries, dtype=float)
fig, ax = plt.subplots()
scatter = ax.scatter(timeseries[:,0], timeseries[:,1], c=orgcolorseries, s = teamseries, alpha = 0.5)

'''plt.plot(speedseries[:,0], np.poly1d(np.polyfit(speedseries[:,0], speedseries[:,1], 1))(speedseries[:,0]))'''

ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Time to Finish in Seconds', fontsize=15)
ax.set_title('Preliminary Buggy Times')
ax.grid(True)
fig.tight_layout()

plt.show()


fig, ax = plt.subplots()
ax.scatter(speedseries[:,0], speedseries[:,1], c=classseries)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Approximate Average Speed (m/s)', fontsize=15)
ax.set_title('Preliminary Buggy Times')

ax.grid(True)
fig.tight_layout()

plt.show()
