
def find_second_largest_num(my_list):
    largest_num = my_list[0]
    second_largest_num = None
    for num in my_list:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num and num < largest_num:
            second_largest_num = num
    return second_largest_num
