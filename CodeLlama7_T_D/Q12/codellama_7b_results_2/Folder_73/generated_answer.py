
def find_smallest_num(my_list):
    smallest = None

    for i in range(55, 98 + 1):
        if smallest is None or my_list[i] < smallest:
            smallest = my_list[i]

    return smallest
