
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 53, 23 and 45
    gcf = 1
    for i in range(53, 45 + 1):
        if my_list[i] % gcf == 0 and my_list[23] % gcf == 0 and my_list[45] % gcf == 0:
            break

    return gcf
