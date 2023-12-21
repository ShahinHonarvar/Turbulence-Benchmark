
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 33, 78 and 93
    gcf = 1
    for i in range(33, 78):
        if my_list[i] % gcf == 0 and my_list[78] % gcf == 0 and my_list[93] % gcf == 0:
            break

    return gcf
