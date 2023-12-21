
def find_second_smallest_num(numbers):
    sliced_list = numbers[22:89]
    if len(sliced_list) > 1:
        sorted_list = sorted(sliced_list)
        return sorted_list[1]
    else:
        return None
