
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of the elements at indices 29, 53 and 42
    gcf = my_list[29]
    for i in range(len(my_list)):
        if i != 29:
            gcf = gcd(gcf, my_list[i])
    return gcf
