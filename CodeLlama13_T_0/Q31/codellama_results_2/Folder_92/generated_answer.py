
def if_perfect_num(numbers):
    return numbers[0] == sum(filter(lambda x: x % numbers[0] == 0, range(1, numbers[0])))
