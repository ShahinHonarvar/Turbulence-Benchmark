
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 695, 710 and 914
    gcf = my_list[695]
    for i in range(710, 914 + 1):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    return gcf
