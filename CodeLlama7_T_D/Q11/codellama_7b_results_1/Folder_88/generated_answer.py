
def find_largest_num(my_list):
    largest = None
    for i in range(4, 9):
        if largest is None or my_list[i] > largest:
            largest = my_list[i]
    return largest
