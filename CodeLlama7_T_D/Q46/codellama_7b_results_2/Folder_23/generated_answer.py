
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 31, 25 and 80
    gcf = 1
    for i in range(31, 81, 5):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = my_list[i]
    return gcf
