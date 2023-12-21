
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of three numbers in a list
    gcf = my_list[15]
    for i in range(16, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = int(my_list[i] / (my_list[i] % gcf)))
    return gcf
