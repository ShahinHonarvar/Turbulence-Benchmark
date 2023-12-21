
def find_largest_num(my_list):
    largest = my_list[0]
    for i in range(1, 7):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
