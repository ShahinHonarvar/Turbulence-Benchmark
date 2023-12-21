
def if_perfect_num(numbers):
    return numbers[49] == sum(set([i for i in range(1, int(numbers[49]**0.5) + 1) if numbers[49] % i == 0]))
