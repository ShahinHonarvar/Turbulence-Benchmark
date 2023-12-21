
def find_smallest_num(my_list):
    smallest = None

    for i in range(527, 538 + 1):
        if smallest == None or my_list[i] < smallest:
            smallest = my_list[i]

    return smallest
