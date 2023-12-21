
def find_second_largest_num(list_of_numbers):
    subset_list = list_of_numbers[22:89]
    if len(subset_list) < 2:
        return None
    subset_list.sort()
    return subset_list[-2]
