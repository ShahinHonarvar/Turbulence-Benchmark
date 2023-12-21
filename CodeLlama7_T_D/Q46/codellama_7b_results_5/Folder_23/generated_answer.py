
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 31, 25 and 80
    gcf = my_list[31]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            break

    return gcf
