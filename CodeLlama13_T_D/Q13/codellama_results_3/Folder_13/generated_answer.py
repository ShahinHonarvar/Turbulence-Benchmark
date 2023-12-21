
def find_second_largest_num(my_list):
    largest_index = 0
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[largest_index]:
            largest_index = i
    second_largest_index = 0
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[second_largest_index] and i != largest_index:
            second_largest_index = i
    return my_list[second_largest_index]
