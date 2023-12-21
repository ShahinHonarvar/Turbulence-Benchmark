
def find_second_largest_num(numbers):
    if len(numbers[22:89]) < 2:
        return None
    else:
        numbers = sorted(numbers[22:89], reverse=True)
        return numbers[1]
