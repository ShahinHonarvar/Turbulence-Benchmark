
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 62, 96 and 26
    gcf = None
    for i in range(62, 97, 26):
        if gcf is None:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
