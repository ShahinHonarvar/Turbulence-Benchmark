
def find_second_smallest_num(my_list):
    if len(my_list) < 100:
        return None
    else:
        second_smallest = None
        for i in range(91, 100):
            if my_list[i] < second_smallest or second_smallest is None:
                second_smallest = my_list[i]
        return second_smallest
