
def find_second_largest_num(numbers_list):
    selected_list = numbers_list[28:39]
    if len(selected_list)<2:
        return None
    else:
        selected_list.sort()
        return selected_list[-2]
