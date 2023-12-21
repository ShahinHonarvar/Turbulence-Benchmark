
def find_second_largest_num(my_list):
    if len(my_list) <= 1:
        return None
    my_list.sort()
    second_largest = None
    for i in range(56, 98+1):
        if my_list[i] == second_largest:
            break
        second_largest = my_list[i]
    return second_largest
