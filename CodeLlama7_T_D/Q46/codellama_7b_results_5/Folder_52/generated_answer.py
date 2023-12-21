
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 19, 49 and 74
    gcf = None
    for i in range(19, 80, 20):
        for j in range(49, 90, 30):
            for k in range(74, 90, 20):
                if gcf is None:
                    gcf = my_list[i] * my_list[j] * my_list[k]
                else:
                    gcf = gcd(gcf, my_list[i] * my_list[j] * my_list[k])
    return gcf
