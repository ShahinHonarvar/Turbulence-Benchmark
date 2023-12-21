
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 19, 94 and 78
    gcf = my_list[19]
    for i in range(19, 94 + 1):
        if gcf == 1:
            break

        else:

            gcf = gcf // my_list[i]

    return gcf
