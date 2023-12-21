
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 28 and 53
    gcf = 1
    for i in range(len(my_list)):
        if i == 99 or i == 28 or i == 53:
            if my_list[i] % gcf == 0:
                continue

            else:

                gcf = my_list[i]

    return gcf
