
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of the elements at indices 90, 84 and 47
    gcf = my_list[90]
    for i in range(1, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
