
def find_smallest_num(my_list):
    smallest = my_list[29]
    for i in range(29, 94):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
