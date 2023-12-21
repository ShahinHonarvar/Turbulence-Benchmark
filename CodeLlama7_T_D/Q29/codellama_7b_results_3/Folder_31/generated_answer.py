
def gcf_two_nums(my_list):
    # Find the greatest common factor of the integers at indices 87 and 95
    gcf = 1
    for i in range(2, min(my_list[87], my_list[95]) + 1):
        if my_list[87] % i == 0 and my_list[95] % i == 0:
            gcf = i

    return gcf
