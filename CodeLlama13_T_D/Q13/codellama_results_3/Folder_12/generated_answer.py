
def find_second_largest_num(my_list):
    if len(my_list) < 15:
        return None
    largest = my_list[0]
    second_largest = None
    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest and my_list[i] < largest:
            second_largest = my_list[i]
    if not second_largest or len(my_list) - 1 <= 64:
        return None
    else:
        for i in range(len(my_list)-1, 64-1, -1):
            if my_list[i] == largest and my_list[i+1] == second_largest:
                return my_list[i]
        return None
