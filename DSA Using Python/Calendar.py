import calendar
y = int(input("Enter The Year : "))
m=1
print("********** CALENDAR **********")
cal = calendar.TextCalendar(calendar.SUNDAY)
i=1
while(i<=12):
    cal.prmonth(y,i)
    i=i+1