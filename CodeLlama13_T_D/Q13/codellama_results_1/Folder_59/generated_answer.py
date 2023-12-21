
def find_second_largest_num(my_list):
    second_largest = None
    largest = my_list[0]
    for i in range(1, 10):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] == largest or my_list[i] < second_largest:
            continue
        else:
            return second_largest
    return None
