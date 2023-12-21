
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 29, 53 and 42
    gcf = 1
    for i in range(29, 53):
        if my_list[i] % gcf == 0:
            continue

        else:

            while my_list[i] % gcf != 0:
                gcf += 1

    return gcf
