
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the three numbers
    gcf = my_list[74]
    for i in range(60, 28 - 1):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = gcf * (my_list[i] / gcf) * (my_list[i + 1] / gcf)
    return gcf
