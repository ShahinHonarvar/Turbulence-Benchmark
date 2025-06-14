
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 21, 51 and 33
    gcf = 1
    for i in range(21, 51 + 1):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
