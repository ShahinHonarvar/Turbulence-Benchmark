
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 70, 98 and 22
    gcf = my_list[70]
    for i in range(71, 98):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = gcf * my_list[i] / (my_list[i] - my_list[i + 1])
    return gcf
