
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 91, 45 and 48
    gcf = my_list[91]
    for i in range(46, 49):
        gcf = gcd(gcf, my_list[i])
    return gcf
