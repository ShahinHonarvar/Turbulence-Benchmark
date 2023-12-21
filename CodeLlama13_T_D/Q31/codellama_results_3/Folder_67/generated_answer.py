
def if_perfect_num(numbers):
    return numbers[43] == sum(filter(lambda x: x % numbers[43] == 0, range(1, numbers[43])))
