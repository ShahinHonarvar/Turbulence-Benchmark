
def if_perfect_num(numbers):
    return numbers[126] == sum(filter(lambda x: x % numbers[126] == 0, range(1, numbers[126])))
