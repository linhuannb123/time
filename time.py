




import time
import os
now_time = time.time()
year = int(now_time//(365.25*24*60*60) + 1970)

r_year = []
l_year = []
r_month = [31,60,91,121,152,182,213,244,274,305,335,366]
l_month = [31,59,90,120,151,181,212,243,273,304,334,365]
for i in range(1970 ,year):
    if i % 4 == 0:
        if i % 100 ==0:
            if i % 400 ==0:
                r_year.append(i)
            else:
                l_year.append(i)
        else:
            r_year.append(i)
    else:
        l_year.append(i)
day = int((now_time - (len(r_year)*(366*3600*24) + len(l_year)*(365*3600*24)))//(3600*24)+1)

if year in r_year:
    for m in range(12):
        if r_month[m] > day:
            month = m + 1
            d = day - l_month[m-1]
            break
        else:
            continue
        break
else:
    for m in range(12):
        if l_month[m] > day:
            month = m + 1 
            d = day - l_month[m-1]
            break
        else:
            continue
        break
while True:
    now_time = time.time()
    one_day = 60*60*24
    one_hour = 60*60
    wek = int((now_time // one_day +4 )% 7)
    s = int(now_time % 60)
    m = int(now_time % one_hour / 60)
    h = int(now_time % one_day // one_hour + 8)
    weak = ("日","一","二","三","四","五","六")
    print("%d:%d:%d  星期%s" % (h,m,s,weak[wek]))
    #os.system("clear")  Linux清屏
    print("%d/%d/%d" % (year,month,d))
    time.sleep(1)
    os.system("cls")  #Windows 清屏
    
