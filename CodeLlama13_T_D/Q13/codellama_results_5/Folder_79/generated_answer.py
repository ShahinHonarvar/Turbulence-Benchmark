
def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    else:
        second_largest = my_list[4]
        for i in range(4, len(my_list)):
            if my_list[i] > second_largest:
                second_largest = my_list[i]
        return second_largest
