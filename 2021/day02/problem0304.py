import sys

if __name__ == '__main__':
    data = [module_mass.split() for module_mass in sys.stdin.readlines()]
    forward = 0
    depth = 0

    for item in data:
        if item[0] == 'forward':
            forward += int(item[1])
        if item[0] == 'up':
            depth = max(depth - int(item[1]), 0)
        if item[0] == 'down':
            depth += int(item[1])

    print(forward * depth)
