
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 34, 38 and 77
    i = 1
    while True:
        if my_list[34] % i == 0 and my_list[38] % i == 0 and my_list[77] % i == 0:
            return i
