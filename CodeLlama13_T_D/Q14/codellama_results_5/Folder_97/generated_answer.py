
def find_second_smallest_num(my_list):
    if len(my_list) < 34:
        return None
    else:
        second_smallest = my_list[31]
        for i in range(32, 35):
            if my_list[i] < second_smallest:
                second_smallest = my_list[i]
        return second_smallest
