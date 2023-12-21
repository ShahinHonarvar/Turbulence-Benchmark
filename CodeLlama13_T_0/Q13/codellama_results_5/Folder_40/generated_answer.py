
def find_second_largest_num(my_list):
    if len(my_list) < 3:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest = sorted_list[2]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != second_largest:
            return second_largest
    return None
