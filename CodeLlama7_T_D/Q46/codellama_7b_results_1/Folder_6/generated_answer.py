
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 93, 94 and 57
    gcf = my_list[93]
    for i in range(94, 57, -1):
        gcf = gcd(gcf, my_list[i])
    return gcf
