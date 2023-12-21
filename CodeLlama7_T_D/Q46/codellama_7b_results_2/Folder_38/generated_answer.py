
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers at indices 14, 21 and 17
    gcf = 1
    for i in range(14, 21 + 1):
        if my_list[i] != 0:
            gcf = my_list[i]
            for j in range(14, 21 + 1):
                while my_list[j] % gcf == 0:
                    my_list[j] //= gcf
    return gcf
