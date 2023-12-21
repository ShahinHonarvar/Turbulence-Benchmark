
def find_second_largest_num(numbers):
    numbers = sorted(numbers)
    for i in range(4, 9):
        if i < len(numbers):
            return numbers[i]
    return None
