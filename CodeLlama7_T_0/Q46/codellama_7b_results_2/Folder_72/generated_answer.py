
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 44, 91 and 42
    gcf = 1
    for i in range(44, 91 + 1):
        if my_list[i] % gcf == 0 and my_list[42] % gcf == 0:
            return gcf

        else:

            gcf += 1

    return -1
