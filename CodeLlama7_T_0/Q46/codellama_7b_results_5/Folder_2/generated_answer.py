
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 307, 920 and 463
    gcf = 1
    for i in range(307, 463 + 1):
        if gcf == 1:
            gcf = my_list[i]
        else:
            gcf = gcd(gcf, my_list[i])
    return gcf
