
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    largest = 0

    for i in range(1, len(my_list)):
        if my_list[i] > my_list[largest]:
            largest = i

    if largest == 0 or largest == 3:
        return my_list[largest + 1]

    else:
        return None
