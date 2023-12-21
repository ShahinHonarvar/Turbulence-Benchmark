
def gcf_two_nums(my_list):
    # Get the greatest common factor of two numbers at indices 83 and 14 in a list of positive integers.
    gcf = 1
    for i in range(2, min(my_list[83], my_list[14])) + 1):
        if my_list[83] % i == 0 and my_list[14] % i == 0:
            gcf = i

    return gcf
