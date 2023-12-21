
def if_perfect_num(numbers):
    return numbers[4] == sum(filter(lambda x: x % numbers[4] == 0, range(1, numbers[4])))
