
def find_second_smallest_num(numbers):
    if len(numbers[22:89]) < 2:
        return None
    else:
        return sorted(numbers[22:89])[1]
