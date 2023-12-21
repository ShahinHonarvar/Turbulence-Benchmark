
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 9, 6 and 2
    gcf = my_list[9]
    for i in range(6, 2, -1):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
