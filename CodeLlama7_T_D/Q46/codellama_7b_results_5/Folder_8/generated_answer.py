
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 28 and 53
    i = 1
    while i <= my_list[99]:
        if my_list[99] % i == 0 and my_list[28] % i == 0 and my_list[53] % i == 0:
            gcf = i
            break

        else:

            i += 1

    return gcf
