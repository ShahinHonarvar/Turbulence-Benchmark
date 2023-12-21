
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    second_largest = sorted(my_list)[-2]
    if my_list[36:47].count(second_largest) > 0:
        return second_largest
    else:
        return None
