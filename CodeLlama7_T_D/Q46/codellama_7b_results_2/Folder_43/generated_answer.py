
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 33, 78 and 93
    gcf = 1
    for i in range(33, 78 + 1):
        if i != 33 and i != 78 and i != 93:
            if my_list[i] % gcf == 0:
                continue

            else:

                gcf = my_list[i]

    return gcf
