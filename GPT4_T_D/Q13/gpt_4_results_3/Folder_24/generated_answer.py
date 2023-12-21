
def find_second_largest_num(numbers):
    if len(numbers[74:96]) < 2:
        return None
    else:
        sorted_nums = sorted(numbers[74:96])
        return sorted_nums[-2]
