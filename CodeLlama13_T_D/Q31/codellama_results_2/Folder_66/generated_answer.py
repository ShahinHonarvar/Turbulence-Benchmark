
def if_perfect_num(numbers):
    return True if numbers[42] == sum(filter(lambda x: x % numbers[42] == 0, range(1, numbers[42]))) else False
