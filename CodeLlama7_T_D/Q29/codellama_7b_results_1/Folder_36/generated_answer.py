
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 429 and 289
    gcf = 1
    for i in range(2, min(my_list[429], my_list[289]) + 1):
        if my_list[429] % i == 0 and my_list[289] % i == 0:
            gcf = i
    return gcf
