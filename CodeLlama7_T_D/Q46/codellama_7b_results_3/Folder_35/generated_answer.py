
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 742, 888 and 629
    gcf = 1
    for i in range(742, 888 + 1):
        if my_list[i] % gcf == 0 and my_list[888] % gcf == 0 and my_list[629] % gcf == 0:
            break

    return gcf
