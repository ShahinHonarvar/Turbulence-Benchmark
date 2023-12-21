
def find_second_smallest_num(numbers):
    if len(numbers[26:53]) < 2:
        return None
    else:
        return sorted(numbers[26:53])[1]
