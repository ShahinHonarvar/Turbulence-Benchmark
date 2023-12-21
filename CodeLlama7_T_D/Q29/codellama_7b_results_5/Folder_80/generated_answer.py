 `def gcf_two_nums(my_list):
    # Initialize variables for greatest common factor and current divisor
    gcf = 1
    div = 2
    # Loop until the greatest common factor is found
    while div <= my_list[95] and div <= my_list[85]:
        if my_list[95] % div == 0 and my_list[85] % div == 0:
            gcf = div
            div += 1
        else:
            div += 1

    return gcf`
