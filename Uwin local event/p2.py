ice_mon = ['JAN', 'FEB', 'MAR', "APR", "MAÍ", "JÚN", "JÚL", "ÁGÚ", "SEP", "OKT", "NÓV","DES"]

date_format = list(input().split("/"))
date = list(date_format[0].split( ))[0]
month = list(date_format[0].split( ))[1]

year = int(list(date_format[1].split( ))[1])
year += 2000

i = ice_mon.index(month)
if( i+1 < 10 ):
    num_mon = "0" + str((i+1));
else:
    num_mon = str((i+1));

print( str(year) + "-" + num_mon + "-" + date)