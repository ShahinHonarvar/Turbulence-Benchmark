
def find_second_smallest_num(my_list):
    if len(my_list) < 93:
        return None
    else:
        second_smallest = my_list[66]
        for i in range(67, 94):
            if my_list[i] < second_smallest:
                second_smallest = my_list[i]
        return second_smallest
