
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 637, 411 and 757
    gcf = 1
    for i in range(637, 757 + 1):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
