
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    for i in range(25, 60):
        if i + 1 < len(sorted_list) and sorted_list[i] == sorted_list[i+1]:
            return None
        elif i + 1 < len(sorted_list):
            return sorted_list[i+1]
    return None
