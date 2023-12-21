
def find_second_largest_num(my_list):
    if len(my_list) < 3:
        return None
    else:
        second_largest = sorted(my_list)[-2]
        return second_largest
