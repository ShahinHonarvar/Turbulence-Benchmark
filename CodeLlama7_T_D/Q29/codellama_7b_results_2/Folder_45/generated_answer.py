
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 47 and 97
    i = 1
    while i <= my_list[47]:
        if my_list[47] % i == 0 and my_list[97] % i == 0:
            gcf = i

    return gcf
