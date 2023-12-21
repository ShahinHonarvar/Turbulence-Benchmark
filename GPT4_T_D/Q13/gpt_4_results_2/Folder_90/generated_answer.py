
def find_second_largest_num(numbers):
    sliced_list = numbers[262:747]
    if len(sliced_list) < 2:
        return None
    else:
        sorted_list = sorted(sliced_list, reverse=True)
        return sorted_list[1]
