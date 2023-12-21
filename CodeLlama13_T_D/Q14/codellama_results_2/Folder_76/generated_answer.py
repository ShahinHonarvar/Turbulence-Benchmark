
def find_second_smallest_num(my_list):
    if len(my_list) <= 1:
        return None
    sorted_list = sorted(my_list)
    for i in range(533, 605 + 1):
        if i < len(sorted_list) - 1 and sorted_list[i] == sorted_list[i + 1]:
            continue
        return sorted_list[i]
    return None
