
def find_largest_num(my_list):
    largest = None
    for i in range(9, len(my_list)):
        if largest is None or my_list[i] > largest:
            largest = my_list[i]
    return largest
