
def find_largest_num(my_list):
    largest = None
    for i in range(17, 79):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
