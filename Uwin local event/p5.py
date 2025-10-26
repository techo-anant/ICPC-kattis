start = list(map(int, input().split(":")))
end = list(map(int, input().split(":")))

hour_diff = end[0] - start[0];
if( end[0] >= 12 and start[0] < 12):
    hour = '1'
else:
    hour ='0'
min_diff = end[1] - start[1];


print(hour + ' ' + str(hour_diff) + " "+ str(hour_diff*60 + min_diff))
