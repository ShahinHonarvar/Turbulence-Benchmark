
def find_smallest_num(my_list):
    smallest = my_list[10]
    for i in range(11, 67):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
