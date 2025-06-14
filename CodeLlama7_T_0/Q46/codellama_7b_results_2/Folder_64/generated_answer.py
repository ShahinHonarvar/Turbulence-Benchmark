
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 0, 8 and 3
    gcf = my_list[0]
    for i in range(1, len(my_list)):
        if i == 8 or i == 3:
            gcf = gcd(gcf, my_list[i])
    return gcf
