
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 637, 411 and 757
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while (my_list[637] * my_list[411]) % my_list[757] == 0:
                gcf = my_list[i]
    return gcf
