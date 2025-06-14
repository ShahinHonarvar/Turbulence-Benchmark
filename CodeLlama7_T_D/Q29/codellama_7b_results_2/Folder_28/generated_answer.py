
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 48 and 76
    gcf = 1
    for i in range(2, min(my_list[48], my_list[76]) + 1):
        if my_list[48] % i == 0 and my_list[76] % i == 0:
            gcf = i

    return gcf
