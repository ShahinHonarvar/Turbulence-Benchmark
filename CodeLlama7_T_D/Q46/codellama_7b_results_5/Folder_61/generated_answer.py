
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 1, 2 and 7
    gcf = my_list[1] * my_list[2] * my_list[7]
    for i in range(min(my_list)):
        if my_list[i] > 0:
            gcf = gcf // gcd(gcf, my_list[i])
    return gcf
