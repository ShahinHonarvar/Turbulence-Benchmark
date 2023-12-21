
def if_perfect_num(numbers):
    return numbers[80] == sum(range(1, int(numbers[80])**0.5 + 1))
