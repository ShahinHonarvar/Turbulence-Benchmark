
def find_largest_num(my_list):
    largest = my_list[1]
    for i in range(2, 9):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
