
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(28, 33):
        if my_list[i] < my_list[27]:
            second_smallest = my_list[i]
            break
    return second_smallest
