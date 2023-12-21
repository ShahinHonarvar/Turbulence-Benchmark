
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 70, 41 and 20
    gcf = 1
    for i in range(70, 20, -1):
        if my_list[i] % gcf == 0 and my_list[41] % gcf == 0 and my_list[20] % gcf == 0:
            break

    return gcf
