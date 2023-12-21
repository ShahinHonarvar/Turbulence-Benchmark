
def find_second_smallest_num(num_list):
    selected_list = num_list[527:539]
    if len(selected_list) < 2:
        return None
    selected_list.sort()
    return selected_list[1]
