
def if_perfect_num(numbers):
    return numbers[13] == sum(filter(lambda x: x % numbers[13] == 0, numbers))
