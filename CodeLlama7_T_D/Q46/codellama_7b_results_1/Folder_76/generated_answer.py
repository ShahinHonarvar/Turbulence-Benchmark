
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[876]
    for i in range(203, 100, -1):
        if my_list[i] % gcf == 0:
            return gcf
