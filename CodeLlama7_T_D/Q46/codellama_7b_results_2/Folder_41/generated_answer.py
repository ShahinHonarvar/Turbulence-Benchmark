
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 19, 94 and 78
    i = 19
    while i <= 94:
        if my_list[i] % my_list[94] != 0 or my_list[i] % my_list[78] != 0:
            i += 1

    else:

        return my_list[i]
