
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    for i in range(20, 201):
        if sorted_list[i] == sorted_list[i-1]:
            return None
    return sorted_list[20]
