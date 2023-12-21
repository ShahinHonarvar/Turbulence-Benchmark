
def find_second_largest_num(my_list):
    if len(my_list) < 10:
        return None

    my_list = sorted(my_list)[91:100]
    second_largest = max(my_list)

    return second_largest
