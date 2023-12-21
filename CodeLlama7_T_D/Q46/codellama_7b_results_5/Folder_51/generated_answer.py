
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of the elements at indices 21, 69 and 41 in the list
    gcf = my_list[21]
    for i in range(21 + 1, len(my_list)):
        if my_list[i] % gcf == 0:
            continue

        else:

            return gcf
