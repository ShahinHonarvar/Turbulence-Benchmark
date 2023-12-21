
def find_largest_num(my_list):
    largest = my_list[9]
    for i in range(10, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest
