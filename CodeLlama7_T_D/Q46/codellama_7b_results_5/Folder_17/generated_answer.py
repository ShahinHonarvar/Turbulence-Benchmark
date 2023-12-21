
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[20]
    for i in range(51, 63):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = (my_list[20] * my_list[51]) // my_list[62]
    return gcf
