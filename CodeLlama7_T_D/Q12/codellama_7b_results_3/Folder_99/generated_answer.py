
def find_smallest_num(my_list):
    smallest = None
    for i in range(409, 743):
        if smallest == None or my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
