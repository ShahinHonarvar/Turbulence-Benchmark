
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers at indices 42 and 25
    gcf = 1
    for i in range(1, min(my_list[42], my_list[25]) + 1):
        if my_list[42] % i == 0 and my_list[25] % i == 0:
            gcf = i

    return gcf
