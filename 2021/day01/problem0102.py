import sys


def it_decreased(prev, actual):
    return True if prev < actual else False


if __name__ == '__main__':
    decreased = 0
    data = [int(module_mass) for module_mass in sys.stdin.readlines()]
    for i in range(1, len(data)):
        if it_decreased(data[i - 1], data[i]):
            decreased += 1
    print(decreased)

    decreased = 0
    sums = []
    for i in range(1, len(data) - 1):
        sums.append((data[i - 1], data[i], data[i + 1]))

    items = [sum(item) for item in sums]

    for i in range(1, len(items)):
        if it_decreased(items[i - 1], items[i]):
            decreased += 1

    print(decreased)
