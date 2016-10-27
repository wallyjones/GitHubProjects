import pytz
from datetime import datetime,time

print("The Current time in Portland Oregon is.....")
PACdate = datetime.now(pytz.timezone('US/Pacific'))
print PACdate

ATLdate = datetime.now(pytz.timezone('America/Indianapolis'))
print("\nThe current time zone in New York is.....")
print ATLdate

LONdate = datetime.now(pytz.timezone('GB'))
print("\nThe current time zone in London is.....")
print LONdate

nineAM = time(9,0,0,0)
ninePM = time(21,0,0,0)

ATL = time(ATLdate.hour,ATLdate.minute)
LON = time(LONdate.hour,LONdate.minute)
PAC = time(PACdate.hour,PACdate.minute)

stop = True
while stop:
    if ATL >= nineAM:
        if ATL <= ninePM:
            print("\nThe store in New York is currently open...")
            print ATL
            print("Portland HQ time...")
            print PAC
            stop = False
        else:
            print("\nSorry the New York store is not open...")
            print ATL
            print("Portland HQ time...")
            print PAC
            stop = False
    if LON >= nineAM:
        if LON <= ninePM:
            print("\nThe store in London is currently open...")
            print LON
            print("Portland HQ time...")
            print PAC
            stop = False
        else:
            print("\nSorry the London store is not open...")
            print LON
            print("Portland HQ time...")
            print PAC
            stop = False
    
