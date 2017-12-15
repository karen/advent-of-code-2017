def solve1(a, b, fA, fB, MOD, n, m):
    cnt = 0
    for j in range(n):
        a = (a*fA) % MOD
        b = (b*fB) % MOD
        if ((a ^ b) & m) == 0:
            cnt += 1
    return cnt

def solve2(a, b, fA, fB, MOD, n, m):
    resA = []
    resB = []
    while len(resA) != n:
        a = (a*fA) % MOD
        if (a % 4) == 0:
            resA.append(a)

    while len(resB) != n:
        b = (b*fB) % MOD
        if (b % 8) == 0:
            resB.append(b)
    
    cnt = 0
    for i in range(len(resA)):
        if ((resA[i] ^ resB[i]) & m) == 0:
            cnt += 1
    return cnt

a = 883
b = 879
fA = 16807
fB = 48271
MOD = 2147483647
m = 0x0000ffff

print(solve1(a, b, fA, fB, MOD, int(40e6), m))
print(solve2(a, b, fA, fB, MOD, int(5e6), m))
