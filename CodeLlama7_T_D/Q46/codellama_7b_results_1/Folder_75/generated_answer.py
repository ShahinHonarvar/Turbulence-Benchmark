
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 70, 98 and 22
    gcf = my_list[70] * my_list[98] * my_list[22]
    for i in range(1, min(my_list[70], my_list[98], my_list[22])) + 1):
        if my_list[70] % i == 0 and my_list[98] % i == 0 and my_list[22] % i == 0:
            gcf = i
    return gcf
