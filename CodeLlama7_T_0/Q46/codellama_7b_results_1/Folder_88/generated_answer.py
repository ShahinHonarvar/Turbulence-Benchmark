
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 47, 10 and 28
    gcf = my_list[47]
    for i in range(10, 28 + 1):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
