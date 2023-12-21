
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 16, 87 and 95
    gcf = my_list[16]
    for i in range(17, 87):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = my_list[i]

    for i in range(88, 95):

        if my_list[i] % gcf == 0:

            continue


        else:


            gcf = my_list[i]


    return gcf
