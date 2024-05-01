from random import randint

with open ("data", "w") as f:
    results = []
    for i in range (100):
        a = randint(0, 1)
        b = randint(0, 1)
        results.append((a, b, (~(a&b))&0x1))
    f.write('\n'.join(list(map(str, results))))
