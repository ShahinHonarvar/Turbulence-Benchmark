
def gcf_two_nums(my_list):
    # Get the greatest common factor of the integers at indices 85 and 33
    gcf = 1
    for i in range(2, min(my_list[85], my_list[33])) + 1):
        if my_list[85] % i == 0 and my_list[33] % i == 0:
            gcf = i
            break

    return gcf
