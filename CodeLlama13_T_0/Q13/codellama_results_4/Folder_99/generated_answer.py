
def find_second_largest_num(my_list):
    if len(my_list) < 310 or len(my_list) > 370:
        return None
    else:
        second_largest = my_list[310]
        for i in range(311, 371):
            if my_list[i] > second_largest:
                second_largest = my_list[i]
        return second_largest
