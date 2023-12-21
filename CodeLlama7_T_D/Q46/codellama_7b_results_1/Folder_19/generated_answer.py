
def gcf_three_nums(my_list):
    # find the greatest common factor of three numbers
    gcf = 1
    for i in range(2, min(my_list[40], my_list[15], my_list[99])) + 1):
        if my_list[40] % i == 0 and my_list[15] % i == 0 and my_list[99] % i == 0:
            gcf = i

    return gcf
