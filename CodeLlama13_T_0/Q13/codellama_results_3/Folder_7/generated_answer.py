
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)[::-1]
    for i in range(661, 924+1):
        if sorted_list[i] != sorted_list[i-1]:
            return sorted_list[i]
    return None
