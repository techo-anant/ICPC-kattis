with open ("1.in", "r") as file:
    lines = file.readlines()

needs = list(map(int, lines[0].split()))
have = list(map(int, lines[1].split()))
can_buy = list(map(int, lines[2].split()))

needed = {
    "r": needs[0] - have[0] if needs[0] > have[0] else 0,
    "g": needs[1] - have[1] if needs[1] > have[1] else 0,
    "b": needs[2] - have[2] if needs[2] > have[2] else 0,
}

if ( needed["r"] > can_buy[0] or needed["b"] > can_buy[1] or needed["g"] > (can_buy[0]+can_buy[1])):
    print(-1);
elif ((needed["r"] + needed["g"] + needed["b"]) > (can_buy[0]+can_buy[1])):
    print(-1);
else:
    print((needed["r"] + needed["g"] + needed["b"]));

exit(); 