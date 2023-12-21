
def find_second_smallest_num(my_list):
    if len(my_list) < 2:
        return None
    second_smallest = my_list[1]
    for i in range(1, len(my_list)):
        if my_list[i] < second_smallest and i >= 19 and i <= 92:
            second_smallest = my_list[i]
    return second_smallest
