
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of the three numbers
    gcf = my_list[18]
    for i in range(10, 76 + 1):
        if gcf > my_list[i]:
            continue

        else:

            gcf = my_list[i]

    return gcf
