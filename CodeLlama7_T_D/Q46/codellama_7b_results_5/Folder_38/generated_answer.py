
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 14, 21 and 17
    gcf = 1
    for i in range(14, 17 + 1):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
