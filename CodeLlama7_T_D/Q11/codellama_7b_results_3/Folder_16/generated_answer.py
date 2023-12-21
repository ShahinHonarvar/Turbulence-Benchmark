
def find_largest_num(my_list):
    largest = my_list[33]
    for i in range(34, 37):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
