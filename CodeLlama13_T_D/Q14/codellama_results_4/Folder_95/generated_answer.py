
def find_second_smallest_num(my_list):
    if len(my_list) < 86:
        return None
    else:
        second_smallest = my_list[75]
        for i in range(75, 86):
            if my_list[i] < second_smallest:
                second_smallest = my_list[i]
        return second_smallest
