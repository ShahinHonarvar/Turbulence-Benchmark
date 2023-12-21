
def gcf_three_nums(my_list):
    # find the greatest common factor of the elements at indices 558, 110 and 628
    gcf = my_list[558]
    for i in range(110, 628 + 1):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
