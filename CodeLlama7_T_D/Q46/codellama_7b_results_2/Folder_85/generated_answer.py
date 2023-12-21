
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of the elements at indices 49, 46 and 13 in the list
    gcf = my_list[49]
    for i in range(len(my_list)):
        if my_list[i] < gcf:
            break

        else:

            gcf = my_list[i]

    return gcf
