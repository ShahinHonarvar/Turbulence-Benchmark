
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[1] * my_list[6] * my_list[8]
    for i in range(2, min(my_list[1], my_list[6], my_list[8])) + 1):
        if my_list[1] % i == 0 and my_list[6] % i == 0 and my_list[8] % i == 0:
            gcf = i

    return gcf
