
def find_smallest_num(my_list):
    smallest = my_list[31]
    for i in range(32, 35):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
