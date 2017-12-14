input1 = "97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190"
input2 = "1,2,3"

def khash(ipt):
    lengths = list(map(ord, ipt))
    suffix = [17, 31, 73, 47, 23]
    lengths = lengths + suffix
    n = 256
    r = list(range(n))
    i, skip = 0, 0
    rounds = 64
    

    for k in range(rounds):
        for l in lengths:
            lo, hi = i, (i + l-1) % len(r)
            cnt = l // 2
            while cnt:
                r[lo], r[hi] = r[hi], r[lo]
                lo = (lo + 1 + len(r)) % len(r)
                hi = (hi - 1 + len(r)) % len(r)
                cnt -=1
            i = (i + l + skip) % len(r)
            skip += 1

    res = [0] * 16
    for m in range(16):
        for p in range(16):
            res[m] ^= r[16 * m + p]

    res = map(lambda x: x[2:], map(hex, res))

    ans = ''
    for hd in res:
        if len(hd) == 2:
            ans += hd
        else:
            ans += '0' + hd

    return {'part1': r[0]*r[1], 'part2': ans}
