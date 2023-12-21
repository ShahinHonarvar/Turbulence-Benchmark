
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 4, 0 and 8
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 1:
            while my_list[i] % gcf == 0 and my_list[4] % gcf == 0 and my_list[0] % gcf == 0 and my_list[8] % gcf == 0:
                gcf = gcf + 1
    return gcf
