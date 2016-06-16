#Usamos libreria TIME para funciones de tiempo

import time
print(time.localtime())
#IMPRIMIRA: time.struct_time(tm_year=2020, tm_mon=2, 
#tm_day=23, tm_hour=22, tm_min=18, tm_sec=39, tm_wday=0, tm_isdst=0)
t = time.localtime()
year = t[0]
month = t[1]
day = t[2]
hour = t[3]
minu = t[4]
sec = t[5]
wday = t[6]
yday = t[7]
isdst = t[8]

print(year, month, day, hour, minu, sec, wday, yday, isdst)
#print(month)
#print(day)
#print(hour)