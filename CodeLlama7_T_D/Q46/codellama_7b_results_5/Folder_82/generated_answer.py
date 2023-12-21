
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 67, 84 and 13
    i = 2
    while i <= min(my_list[67], my_list[84], my_list[13])):
        if all(x % i == 0 for x in [my_list[67], my_list[84], my_list[13]])):
            gcf = i
            break

        else:

            i += 1

    return gcf
