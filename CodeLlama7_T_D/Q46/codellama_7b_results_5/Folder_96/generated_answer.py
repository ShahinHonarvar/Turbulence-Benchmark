
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 29, 74 and 49
    gcf = my_list[29]
    for i in range(30, len(my_list)):
        gcf = gcd(gcf, my_list[i])
    return gcf
