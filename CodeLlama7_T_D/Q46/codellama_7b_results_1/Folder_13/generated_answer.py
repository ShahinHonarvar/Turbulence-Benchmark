
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 991, 244 and 974
    gcf = 1
    for i in range(gcf, my_list[991] + 1):
        if my_list[991] % i == 0 and my_list[244] % i == 0 and my_list[974] % i == 0:
            gcf = i

    return gcf
