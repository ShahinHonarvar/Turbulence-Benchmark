
def find_largest_num(my_list):
    largest_num = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > largest_num:
            largest_num = my_list[i]
    return largest_num
