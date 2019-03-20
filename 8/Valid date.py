sec=int(input("sec"))
min=int(input("min"))
hour=int(input("hour"))
day=int(input("day"))
month=int(input("month"))
year=int(input("year"))
monthMaxDay=[31,28,31,30,31,30,31,31,30,31,30,31]
def validSec(sec):
    if sec<0:
        return False
    elif sec>60:
        return False
    else:
        return True
def validMin(min):
    if min<0:
        return False
    elif min>60:
        return False
    else:
        return True
def validHour(hour):
    if hour<0:
        return False
    elif hour>24:
        return False
    else:
        return True
def validDate(date,month,year):
    if year<0:
        return Flase
    elif month<0:
        return False
    elif month>12:
        return False
    elif date<0:
        return False
    elif month!=2:
        if day<=monthMaxDay[month+1]:
            return True
    elif day<=28:
        return True
    elif year%4==0:
        if day<=29:
            return True
        else:
            return False
    else:
        return False
print(validSec(sec) and validMin(min)and validHour(hour)and validDate(day,month,year))

        
