
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 634 and 585
    i = 2
    while i <= my_list[634] and i <= my_list[585]:
        if my_list[634] % i == 0 and my_list[585] % i == 0:
            gcf = i
            i += 1

    return gcf
