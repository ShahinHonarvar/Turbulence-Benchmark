
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[29], my_list[53]) + 1):
        if my_list[29] % i == 0 and my_list[53] % i == 0:
            gcf = i

    return gcf
