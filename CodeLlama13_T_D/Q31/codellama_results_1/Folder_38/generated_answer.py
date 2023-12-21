
def is_perfect_num(numbers):
    return numbers[38] == sum(range(1, int(numbers[38]) + 1)) - numbers[38]
