
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(22, 51):
        if my_list[i] < my_list[i-1]:
            second_smallest = my_list[i-1]
    return second_smallest
