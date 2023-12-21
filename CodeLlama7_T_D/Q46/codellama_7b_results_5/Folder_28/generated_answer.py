
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 99, 63 and 74
    gcf = None
    for i in range(99, 75):
        if gcf is None:
            gcf = my_list[i]
        else:
            while my_list[i] % gcf != 0:
                gcf -= 1
    return gcf
