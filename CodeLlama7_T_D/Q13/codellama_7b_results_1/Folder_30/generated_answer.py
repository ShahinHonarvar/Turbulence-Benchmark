 def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    second_largest = None

    for i in range(55, 99 + 1):
        if my_list[i] > second_largest or second_largest == None:
            second_largest = my_list[i]

    return second_largest
