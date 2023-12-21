
def if_perfect_num(numbers):
    return numbers[72] == sum(range(1, int(numbers[72])**0.5 + 1)) and all(numbers[72] % i for i in range(1, int(numbers[72]**0.5) + 1) if i ** 2 != numbers[72])
