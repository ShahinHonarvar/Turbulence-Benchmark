
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    if len(sorted_list) <= 1:
        return None
    else:
        second_smallest = sorted_list[82]
        for i in range(83, 87):
            if sorted_list[i] < second_smallest:
                second_smallest = sorted_list[i]
        return second_smallest
