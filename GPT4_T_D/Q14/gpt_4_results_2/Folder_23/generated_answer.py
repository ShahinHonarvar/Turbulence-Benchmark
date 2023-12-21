
def find_second_smallest_num(numbers):
    if len(numbers[19:93]) < 2:
        return None
    else:
        return sorted(numbers[19:93])[1]
