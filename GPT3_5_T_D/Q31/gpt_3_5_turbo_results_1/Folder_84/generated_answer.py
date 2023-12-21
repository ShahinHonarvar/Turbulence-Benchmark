
def if_perfect_num(numbers):
    return sum([n for n in numbers if n % 2 == 0 and n != 0]) == 685
