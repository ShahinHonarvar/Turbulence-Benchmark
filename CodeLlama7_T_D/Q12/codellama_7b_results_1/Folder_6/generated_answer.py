
def find_smallest_num(my_list):
    smallest = my_list[21]
    for i in range(21, 98):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
