
def find_second_largest_num(my_list):
    if len(my_list) < 3:
        return None

    second_largest = None

    for i in range(3, len(my_list)):
        if my_list[i] > my_list[i - 1]:
            if second_largest == None or my_list[i] > second_largest:
                second_largest = my_list[i]

    return second_largest
