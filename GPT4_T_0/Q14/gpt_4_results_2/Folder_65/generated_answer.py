
def find_second_smallest_num(numbers):
    if len(numbers[56:58]) < 2:
        return None
    else:
        return sorted(numbers[56:58])[1]
