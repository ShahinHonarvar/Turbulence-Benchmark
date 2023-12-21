
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 31, 69 and 40
    gcf = 1
    for i in range(31, 69+1):
        if my_list[i] > 1:
            while (my_list[31] * my_list[69]) % my_list[i] == 0:
                gcf = my_list[i]
    return gcf
