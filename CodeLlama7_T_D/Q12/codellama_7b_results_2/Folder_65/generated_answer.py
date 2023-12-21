
def find_smallest_num(my_list):
    smallest = my_list[12]
    for i in range(13, 93):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest
