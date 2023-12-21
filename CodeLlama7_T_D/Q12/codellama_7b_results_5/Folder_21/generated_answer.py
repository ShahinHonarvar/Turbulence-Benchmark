
def find_smallest_num(my_list):
    smallest = my_list[686]
    for i in range(687, 987 + 1):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
