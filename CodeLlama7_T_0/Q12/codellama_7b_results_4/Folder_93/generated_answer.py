
def find_smallest_num(my_list):
    smallest = None

    for i in range(29, 94):
        if smallest is None or my_list[i] < smallest:
            smallest = my_list[i]

    return smallest
