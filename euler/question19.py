from datetime import datetime,date,timedelta;
#1 Jan 1900
v_date=date(1900,1,1);
print v_date,v_date.day,v_date.month
#date.month=date.__add__()
v_date2=date(v_date.year,v_date.month+1,1);
print v_date2
d=v_date2-v_date
print d
print v_date2.weekday()

print date(2012,10,29).weekday()
count=0;
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
for count_year in xrange(1901,2001):
    for count_month in xrange(1,13):
       if date(count_year,count_month,1).weekday()==6:
            count+=1;
print count
