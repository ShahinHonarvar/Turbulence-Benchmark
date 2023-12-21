
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 37, 30 and 48
    gcf = 1
    for i in range(37, 49):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
