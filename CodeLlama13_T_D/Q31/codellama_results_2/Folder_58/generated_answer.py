
def if_perfect_num(numbers):
    return numbers[714] == sum(filter(lambda x: x % numbers[714] == 0, range(1, numbers[714])))
