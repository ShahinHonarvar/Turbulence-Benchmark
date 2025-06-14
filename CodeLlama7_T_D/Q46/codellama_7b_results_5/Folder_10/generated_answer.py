
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    gcf = my_list[86]
    for i in range(87, 90):
        gcf = gcd(gcf, my_list[i])
    for i in range(48, 50):
        gcf = gcd(gcf, my_list[i])
    return gcf
