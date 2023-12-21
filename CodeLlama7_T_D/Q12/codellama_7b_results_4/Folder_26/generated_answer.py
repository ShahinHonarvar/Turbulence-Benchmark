
def find_smallest_num(my_list):
    smallest = my_list[28]
    for i in range(29, 39):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
