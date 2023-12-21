
def if_perfect_num(numbers):
    return numbers[90] == sum(filter(lambda x: x % numbers[90] == 0, range(1, numbers[90])))
