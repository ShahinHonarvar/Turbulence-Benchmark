
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 49, 46 and 13
    gcf = my_list[49]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
