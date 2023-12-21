
def find_largest_num(my_list):
    largest = my_list[246]
    for i in range(247, 751):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
