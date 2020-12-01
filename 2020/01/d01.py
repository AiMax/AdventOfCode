import sys

if __name__ == '__main__':
    numbers = [int(number) for number in sys.stdin.readlines()]

# part 1

    for i in range(len(numbers)):
        for num in numbers[i:]:
            if numbers[i] + num == 2020:
                print(numbers[i] * num)

# part 2

    for i in range(len(numbers)):
        for j in range(len(numbers[i:])):
            for k in range(len(numbers[j:])):
                if (numbers[i] + numbers[j] + numbers[k]) == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])
