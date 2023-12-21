
def gcf_three_nums(my_list):
    # find the greatest common factor of three numbers
    gcf = 1
    for i in range(2, min(my_list[76], my_list[64], my_list[28])) + 1):
        if my_list[76] % i == 0 and my_list[64] % i == 0 and my_list[28] % i == 0:
            gcf = i
    return gcf
