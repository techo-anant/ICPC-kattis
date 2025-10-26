n = int(input())

additional = list(map(int, input().split()))
can_solve = list(map(int, input().split()))

best_guardians = sorted(can_solve);

max_avg = 0;

for i in range(n):
    avg = (sum(best_guardians[:(i+1)])+ additional[i])/(i+1)
    if( avg > max_avg):
        max_avg = avg;

print(max_avg)