
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers at indices 24, 45 and 38 in a list of positive integers
    gcf = my_list[24]
    for i in range(25, 45):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = (my_list[i] // gcf) * gcf

    for i in range(46, 38, -1):

        if my_list[i] % gcf == 0:

            continue


        else:


            gcf = (my_list[i] // gcf) * gcf

    return gcf
