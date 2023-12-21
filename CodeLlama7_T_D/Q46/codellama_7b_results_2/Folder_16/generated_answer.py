
def gcf_three_nums(my_list):
    # Extract the elements at indices 558, 110 and 628 from the list
    num_1 = my_list[558]
    num_2 = my_list[110]
    num_3 = my_list[628]
    # Find the greatest common factor of the three numbers
    gcf = 1

    for i in range(2, min(num_1, num_2, num_3) + 1):
        if num_1 % i == 0 and num_2 % i == 0 and num_3 % i == 0:
            gcf = i

    return gcf
