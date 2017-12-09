blocks=[0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]
#blocks=[0,2,7,0]
#blocks=[10, 9, 8, 7, 6, 5, 4, 3, 1, 1, 0, 15, 14, 13, 11, 12]

def solve(blocks):
    curr = tuple(blocks)
    seen = set()
    while curr not in seen:
        seen.add(curr)
        im, iv = 0, blocks[0]
        for i, v in enumerate(blocks):
            if v > iv:
                im = i
                iv = v
        blocks[im] = 0
        while iv > 0:
            im = (im + 1) % len(blocks)
            blocks[im] += 1
            iv -= 1
        curr = tuple(blocks)
    return len(seen)

print(solve(blocks))
print(solve(blocks))
