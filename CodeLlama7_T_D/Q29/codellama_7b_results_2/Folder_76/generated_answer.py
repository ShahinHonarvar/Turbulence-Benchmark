
def gcf_two_nums(my_list):
    # Find the greatest common factor of the integers at indices 184 and 307
    gcf = 1
    for i in range(2, min(my_list[184], my_list[307]) + 1):
        if my_list[184] % i == 0 and my_list[307] % i == 0:
            gcf = i
    return gcf
