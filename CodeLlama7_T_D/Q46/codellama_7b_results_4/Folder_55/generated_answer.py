
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 9, 6 and 2
    gcf = None
    for i in range(len(my_list)):
        if i == 9 or i == 6 or i == 2:
            if gcf is None:
                gcf = my_list[i]
            else:
                while my_list[i] % gcf != 0:
                    gcf -= 1
    return gcf
