
def find_second_largest_num(numbers):
    if len(numbers[90:91]) < 2:
        return None
    else:
        return sorted(numbers[90:91])[-2]
