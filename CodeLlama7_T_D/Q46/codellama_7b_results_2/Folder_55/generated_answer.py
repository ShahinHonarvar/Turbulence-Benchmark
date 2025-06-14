
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 9, 6 and 2
    gcf = 1
    for i in range(3):
        a = my_list[i*3]
        b = my_list[i*3 + 1]
        c = my_list[i*3 + 2]
        # Calculate the greatest common factor of a, b and c
        gcf_abc = gcd(gcd(a, b), c)
        # Update the greatest common factor
        gcf = lcm(gcf, gcf_abc)
    return gcf
