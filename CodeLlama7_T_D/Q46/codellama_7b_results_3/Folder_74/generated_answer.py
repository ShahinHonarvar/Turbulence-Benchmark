
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 99, 95 and 80
    gcf = 1
    for i in range(2, min(my_list[99], my_list[95], my_list[80])) + 1):
        if my_list[99] % i == 0 and my_list[95] % i == 0 and my_list[80] % i == 0:
            gcf = i

    return gcf
