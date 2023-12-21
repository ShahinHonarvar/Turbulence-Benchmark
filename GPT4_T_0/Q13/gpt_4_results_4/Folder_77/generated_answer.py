
def find_second_largest_num(num_list):
    if len(num_list) < 539:
        return None
    else:
        sub_list = num_list[527:539]
        sub_list.sort()
        return sub_list[-2]
