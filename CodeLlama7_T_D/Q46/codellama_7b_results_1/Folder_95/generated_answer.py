
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of the elements at indices 87, 20 and 36
    gcf = my_list[87]
    for i in range(86, -1, -1):
        if my_list[i] % my_list[87] == 0:
            gcf = my_list[i]
            break

    return gcf
