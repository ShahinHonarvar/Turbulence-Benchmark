
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 13, 70 and 32
    gcf = my_list[13]
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while (my_list[i] % gcf) == 0:
                gcf = gcf / (my_list[i] % gcf)
    return gcf
