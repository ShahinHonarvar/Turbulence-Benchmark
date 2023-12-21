
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 24, 25 and 80
    gcf = 1
    for i in range(24, 81, 5):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
