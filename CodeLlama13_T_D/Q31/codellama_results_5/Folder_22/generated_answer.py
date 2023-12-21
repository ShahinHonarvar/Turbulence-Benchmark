
def if_perfect_num(numbers):
    return numbers[72] == sum(filter(lambda x: x % numbers[72] == 0, range(1, numbers[72]+1)))
