import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime


#https://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

timedata=[]
tempdata=[]
for line in open("temp.dat").readlines():
    datetmp=datetime.datetime.strptime(line.split()[0]+" "+line.split()[1],"\"%d/%m/%Y %H:%M:%S\"")

    timedata.append(datetmp)
    tempdata.append(np.float(line.split()[2]))
    #print(timedata)
    #print(datetime.datetime(line.split()[0]+" "+line.split()[1]))

from matplotlib.ticker import FormatStrFormatter

fig, ax = plt.subplots()

print(tempdata)
plt.plot(timedata,tempdata)
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.gcf().autofmt_xdate()

plt.xlabel('Date')
plt.xlabel(r"$Temp ({}^{\circ} C)$")
plt.show()


