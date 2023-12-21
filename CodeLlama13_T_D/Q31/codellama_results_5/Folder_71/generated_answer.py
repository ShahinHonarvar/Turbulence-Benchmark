
def if_perfect_num(numbers):
    return numbers[78] % 2 == 0 and sum(factors(numbers[78])) == numbers[78]
