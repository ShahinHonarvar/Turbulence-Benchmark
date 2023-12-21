
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 37, 30 and 48
    gcf = my_list[37]
    for i in range(len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            gcf = gcf * (my_list[i] / gcf)

    return gcf
