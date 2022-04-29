import math
import sys

# Check the power consumption
# gamma rate and epsilon rate
# Power consumption = gamma rate * epsilon rate
# gamma rate it's the most common bit in the corresponding position
if __name__ == '__main__':
    data = [module_mass.rstrip('\n') for module_mass in sys.stdin.readlines()]
    gamma = ""
    epsilon = ""

    print(data)

    for i in range(len(data[0])):

        one = 0
        zero = 0
        for j in range(len(data)):
            if data[j][i] == '1':
                one += 1
            else:
                zero += 1
        if one > zero:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)

        calc_gamma = int(gamma, 2)
        calc_epsilon = int(epsilon, 2)

    print(calc_gamma)
    print(calc_epsilon)

    print(calc_gamma*calc_epsilon)
