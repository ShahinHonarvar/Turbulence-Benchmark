
def find_largest_num(my_list):
    largest_num = my_list[22]
    for i in range(23, 89):
        if my_list[i] > largest_num:
            largest_num = my_list[i]
    return largest_num
