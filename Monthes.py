import calendar
a=calendar.month_name
for i, month in enumerate(a[1:],start =1):
    print(f"{i},{month}")