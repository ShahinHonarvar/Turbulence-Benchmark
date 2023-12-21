
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    for i in range(29, 80):
        if sorted_list[i] != sorted_list[i-1]:
            return sorted_list[i]
    return None
