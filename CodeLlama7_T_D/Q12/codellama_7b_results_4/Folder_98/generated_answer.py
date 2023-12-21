
def find_smallest_num(my_list):
    smallest = my_list[0]
    for i in range(1, 6):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
