
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 56, 88 and 51
    gcf = 1
    for i in range(56, 89, 3):
        for j in range(i + 3, 90, 3):
            if my_list[i] * my_list[j] > gcf:
                gcf = my_list[i] * my_list[j]
    return gcf
