
def find_second_smallest_num(my_list):
    second_smallest = None
    for i in range(28, 41):
        if my_list[i] < my_list[27]:
            continue
        elif my_list[i] > my_list[27] and my_list[i] <= my_list[40]:
            second_smallest = my_list[i]
    return second_smallest
