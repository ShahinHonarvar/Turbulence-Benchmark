
def if_perfect_num(numbers):
    return numbers[27] == sum(filter(lambda x: x % numbers[27] == 0, range(1, numbers[27]+1)))
