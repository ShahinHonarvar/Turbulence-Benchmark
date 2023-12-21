
def find_second_largest_num(my_list):
    largest_num = my_list[22:63][-1]
    second_largest_num = None
    for num in my_list[22:63]:
        if num > largest_num and num != largest_num:
            second_largest_num = largest_num
            largest_num = num
    return second_largest_num
