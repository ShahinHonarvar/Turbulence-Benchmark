
def find_second_smallest_num(my_list):
    my_list = sorted(my_list)
    for i in range(28, 40+1):
        if my_list[i-1] != my_list[i]:
            return my_list[i]
    return None
