
def find_second_largest_num(my_list):
    largest_num = None
    second_largest_num = None
    for num in my_list:
        if largest_num is None or num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif second_largest_num is None or num > second_largest_num:
            second_largest_num = num
    return second_largest_num
