def nex(curr, ignore, garbage, gp, total, gbc):
    if ignore:
        ignore = False
    elif garbage:
        if curr == '>':
            garbage = False
        elif curr == '!':
            ignore = True
        else:
            gbc += 1
    elif curr == '{':
        gp += 1
    elif curr == '}':
        gp -= 1
        total += gp
    elif curr == '<':
        garbage = True
    return (ignore, garbage, gp, total, gbc)

if __name__ == '__main__':
    with open('aoc9.txt', 'r') as f:
        ignore, garbage = False, False
        gp, total, gbc = 1, 0, 0
        while True:
            c = f.read(1)
            if not c:
                break
            ignore, garbage, gp, total, gbc = nex(c, ignore, garbage, gp, total, gbc)

print(total)
print(gbc)


