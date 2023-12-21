
def gcf_two_nums(my_list):
    # Find the greatest common factor of the integers at indices 28 and 17
    gcf = 1
    for i in range(2, min(my_list[28], my_list[17]) + 1):
        if my_list[28] % i == 0 and my_list[17] % i == 0:
            gcf = i

    return gcf
