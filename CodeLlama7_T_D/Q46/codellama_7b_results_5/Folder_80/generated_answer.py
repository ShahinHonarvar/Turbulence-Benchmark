
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers at specific indices in a list
    gcf = my_list[13]
    for i in range(76, 44, -1):
        if my_list[i] % gcf == 0:
            return gcf

        else:

            gcf = (my_list[i] // gcf) * gcf

    return gcf
