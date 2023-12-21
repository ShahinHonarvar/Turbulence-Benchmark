
def find_second_largest_num(my_list):
    if len(my_list) < 6:
        return None
    second_largest = sorted(my_list)[-2]
    for i in range(5):
        if my_list[i] == second_largest:
            return second_largest
    return None
