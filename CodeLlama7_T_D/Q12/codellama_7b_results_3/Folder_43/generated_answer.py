
def find_smallest_num(my_list):
    smallest = my_list[23]
    for i in range(24, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
