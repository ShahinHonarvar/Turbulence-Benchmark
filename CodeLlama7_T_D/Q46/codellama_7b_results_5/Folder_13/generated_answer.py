
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers
    gcf = my_list[991]
    for i in range(244, 975):
        if my_list[i] % gcf == 0:
            return gcf
    return 1
