
def find_second_smallest_num(numbers):
    if len(numbers[74:96]) < 2:
        return None
    else:
        return sorted(numbers[74:96])[1]
