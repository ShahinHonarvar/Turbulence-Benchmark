
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 944, 814 and 865
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while (my_list[944] * my_list[814]) % my_list[865] != 0:
                my_list[i] -= 1
    return gcf
