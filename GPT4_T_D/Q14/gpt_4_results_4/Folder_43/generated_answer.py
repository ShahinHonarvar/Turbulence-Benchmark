
def find_second_smallest_num(numbers):
    if len(numbers[74:96]) < 2:
        return None
    else:
        sorted_list = sorted(numbers[74:96])
        return sorted_list[1]
