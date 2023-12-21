
def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    sorted_list = sorted(my_list, reverse=True)
    second_largest = sorted_list[3]
    if second_largest == my_list[2]:
        return None
    else:
        return second_largest
