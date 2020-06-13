import xlrd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import pandas as pd
from datetime import datetime
from datetime import timedelta
import getopt

xl = pd.read_excel('demo_model.xlsx', sheet_name= "Model P&L" , index_col = 14, usecols = "N:CG", skiprows=4, nrows = 7);

dates_x = xl.iloc[0, :]
#print(dates_x)
dt_arr = [0]

for jj in range(0, len(dates_x._index)):
    dt = dates_x._index[jj]
    dt_month= dt.month
    dt_daysm= dt.day
    dt_daysa = dt.days_in_month
    dt_diff = dt_daysa - dt_daysm
    if dt_diff != 0:
        dt = dt + timedelta(days = dt_diff)
    dt_arr.insert(jj, dt)

sub_rev = xl.iloc[5, :]
serv_rev = xl.iloc[6, :]


indx_x = np.arange(len(dates_x._index))
tickvalues = np.arange(0,len(dt_arr))

plt.figure(figsize=(25,7))
graphSub = plt.bar(x=indx_x, height=sub_rev, width=0.55)
graphServ = plt.bar(x=indx_x, height=serv_rev, width=0.55, bottom=sub_rev)

plt.gcf().autofmt_xdate()
plt.gca().tick_params(axis='x', which='major', labelsize = 6)

plt.xlabel ('Dates')
plt.ylabel ('Revenue')
plt.title('Demo Company - P&L Model')
plt.xticks(tickvalues, dt_arr)
plt.yticks()
plt.legend((graphSub[0], graphServ[0]), ('Subscription Revenue', 'Service Revenue'))
plt.tight_layout()
plt.show()
