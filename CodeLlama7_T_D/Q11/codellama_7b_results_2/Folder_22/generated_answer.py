
def find_largest_num(my_list):
    largest = None

    for i in range(40, 201):
        if largest is None or my_list[i] > largest:
            largest = my_list[i]

    return largest
