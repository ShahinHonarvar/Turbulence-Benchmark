
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 32, 54 and 13
    gcf = my_list[32]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
