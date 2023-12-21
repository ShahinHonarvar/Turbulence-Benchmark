
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[74] * my_list[60] * my_list[28]
    for i in range(1, min(gcf, 50))):
        if gcf % i == 0:
            return i

    return 1
