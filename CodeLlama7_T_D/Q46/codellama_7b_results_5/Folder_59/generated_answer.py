
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 7, 6 and 8
    gcf = my_list[7]
    for i in range(len(my_list)):
        if i != 7:
            gcf = gcd(gcf, my_list[i])
    return gcf
