import sys

if __name__ == '__main__':
    data = []
    valids = 0
    for line in sys.stdin.readlines():
        a, b, c = line.split(' ')
        min_instances, max_instances = a.split('-')
        if c[-1] == '\n':
            c = c[:-1]
        data.append((int(min_instances), int(max_instances), b[:-1], c))

    # part 1
    for min_p, max_p, character, pwd in data:
        count = 0
        for x in list(pwd):
            if x == character:
                count += 1
                if count > max_p:
                    break

        if min_p <= count <= max_p:
            print(min_p, count, max_p)
            valids += 1
    print(valids)

    # part 2
    valids = 0
    for min_p, max_p, character, pwd in data:
        l = list(pwd)
        if l[min_p - 1] == character or l[max_p - 1] == character:
            if l[min_p - 1] != l[max_p - 1]:
                valids += 1
    print(valids)
