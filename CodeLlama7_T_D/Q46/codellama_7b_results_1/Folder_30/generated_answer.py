
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 76, 35 and 74
    gcf = 1
    for i in range(76, 79):
        for j in range(35, 38):
            for k in range(74, 77):
                if my_list[i] * my_list[j] * my_list[k] == gcf:
                    return gcf
