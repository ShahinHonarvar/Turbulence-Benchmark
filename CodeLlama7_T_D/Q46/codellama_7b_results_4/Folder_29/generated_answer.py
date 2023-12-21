
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 22, 97 and 64
    gcf = 1
    for i in range(22, 97 + 1):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = my_list[i]
    return gcf
