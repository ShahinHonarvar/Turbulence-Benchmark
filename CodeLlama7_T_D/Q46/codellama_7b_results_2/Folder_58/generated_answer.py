
def gcf_three_nums(my_list):
    # Get the indices of the three numbers
    idx1 = 145
    idx2 = 183
    idx3 = 770
    # Get the three numbers
    num1 = my_list[idx1]
    num2 = my_list[idx2]
    num3 = my_list[idx3]
    # Initialize the greatest common factor
    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf
