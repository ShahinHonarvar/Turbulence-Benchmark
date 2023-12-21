
def find_second_smallest_num(numbers):
    if len(numbers[29:94]) < 2:
        return None
    else:
        return sorted(numbers[29:94])[1]
