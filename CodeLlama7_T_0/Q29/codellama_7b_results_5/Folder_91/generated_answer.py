
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 4 and 0
    gcf = 1
    for i in range(2, min(my_list[4], my_list[0]) + 1):
        if my_list[4] % i == 0 and my_list[0] % i == 0:
            gcf = i

    return gcf
