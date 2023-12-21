
def if_perfect_num(numbers):
    return numbers[51] == sum(filter(lambda x: x % numbers[51] == 0, range(2, numbers[51])))
