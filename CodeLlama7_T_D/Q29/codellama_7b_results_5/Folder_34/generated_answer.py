
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 60 and 64
    gcf = 1
    for i in range(2, min(my_list[60], my_list[64]) + 1):
        if my_list[60] % i == 0 and my_list[64] % i == 0:
            gcf = i
    return gcf
