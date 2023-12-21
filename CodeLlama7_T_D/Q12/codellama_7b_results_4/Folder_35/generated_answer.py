
def find_smallest_num(my_list):
    smallest = float('inf')
    for i in range(43, 87):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
