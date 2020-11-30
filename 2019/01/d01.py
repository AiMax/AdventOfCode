import sys


def calculate_fuel(mass):
    return max(0, (mass // 3) - 2)


def calculate_fuel_req(amount):
    current = calculate_fuel(amount)
    if current == 0:
        return 0
    else:
        return calculate_fuel_req(current) + current


if __name__ == '__main__':
    # Part 1
    data = [int(module_mass) for module_mass in sys.stdin.readlines()]
    all_fuel = 0
    for m in data:
        all_fuel += calculate_fuel(m)
    print(all_fuel)

    # Part 2
    print(sum([calculate_fuel_req(item) for item in data]))
