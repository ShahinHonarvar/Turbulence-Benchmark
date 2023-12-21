
def find_second_largest_num(numbers):
    numbers_between_68_and_86 = numbers[68:87]
    if len(numbers_between_68_and_86) < 2:
        return None
    numbers_between_68_and_86.sort()
    return numbers_between_68_and_86[-2]
