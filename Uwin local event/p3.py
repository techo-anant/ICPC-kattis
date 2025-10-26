cases = int(input())
cross = []
for _ in range(cases):
    length, num = map(int, input().split());
    length = 100*length
    crossed = 0
    is_left = True
    left, right = [], []
    for _ in range(num):
        upcoming = list(input().split())
        if ( upcoming[1] == "left"):
            left.append(int(upcoming[0]))
        else:
            right.append(int(upcoming[0]))
    while ( left != [] or right !=[]):
        sum = 0
        if( left !=[] and is_left ):
            sum += left.pop(0);
            while( left != [] and (sum+left[0]) <= length):
                sum += left.pop(0);
            crossed += 1;
            is_left = False;
        elif( right != [] and is_left==False):
            sum += right.pop(0);
            while( right != [] and (sum+right[0]) <= length):
                sum += right.pop(0);
            crossed += 1;
            is_left = True;
        elif(right == [] and is_left==False):
            is_left = True;
            crossed+= 1;
        elif(left == [] and is_left==True):
            is_left = False;
            crossed+= 1;
    cross.append(crossed)

for _ in range(cases):
    print(cross.pop(0))