import sys


def calculate_fueel(mass):
    return max(0, (mass // 3) - 2)


if __name__ == '__main__':

    # for a, b in [(12, 2), (14, 2), (1969, 654), (100756, 33583)]:
    #     print("Masa: {}, Valor: {}, Resultado: {}".format(a, b, calculate_fueel(a)))

    data = [int(module_mass) for module_mass in sys.stdin.readlines()]

    all_fueel = 0

    for mass in data:
        fueel = calculate_fueel(mass)
        print("Masa: {}, Resultado: {}".format(mass, fueel))
        all_fueel += fueel

    print(all_fueel)