
def find_second_smallest_num(numbers):
    if len(numbers[262:747]) < 2:
        return None
    else:
        return sorted(numbers[262:747])[1]
