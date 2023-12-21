
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    second_largest = None
    for i in range(82, 87):
        if i < len(my_list):
            second_largest = my_list[i]
    return second_largest
