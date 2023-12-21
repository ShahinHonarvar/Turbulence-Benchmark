
def find_second_largest_num(my_list):
    second_largest = None
    for i in range(26, 53):
        if my_list[i] > second_largest:
            second_largest = my_list[i]
    return second_largest
