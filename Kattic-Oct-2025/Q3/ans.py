proposed, accept = map(int, input().split());

difficulties = [];
for _ in range(proposed):
    difficulties.append(input())

unique = len(set(difficulties))
if ( unique < accept):
    print(unique)
else:
    print(accept)