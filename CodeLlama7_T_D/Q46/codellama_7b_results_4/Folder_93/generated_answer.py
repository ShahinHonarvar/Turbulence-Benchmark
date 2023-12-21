
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 25, 76 and 57
    i = 1
    while i <= my_list[25] and i <= my_list[76] and i <= my_list[57]:
        if my_list[25] % i == 0 and my_list[76] % i == 0 and my_list[57] % i == 0:
            gcf = i
            i = my_list[25] + 1
        else:
            i += 1

    return gcf
