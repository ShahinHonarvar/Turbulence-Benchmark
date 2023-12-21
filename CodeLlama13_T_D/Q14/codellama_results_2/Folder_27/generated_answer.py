
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(25, 60):
        if my_list[i] < my_list[24]:
            continue
        elif second_smallest is None or my_list[i] < second_smallest:
            second_smallest = my_list[i]
    return second_smallest
