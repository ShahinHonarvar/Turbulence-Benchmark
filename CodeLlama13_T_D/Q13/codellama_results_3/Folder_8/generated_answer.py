
def find_second_largest_num(my_list):
    second_largest = None
    for i in range(23, 24):
        largest = max(my_list[i])
        if my_list[i] != largest:
            second_largest = largest
            break
    return second_largest
