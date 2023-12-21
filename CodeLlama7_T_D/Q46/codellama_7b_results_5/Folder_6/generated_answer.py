
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 93, 94 and 57
    gcf = 1
    for i in range(93, 95):
        for j in range(94, 96):
            for k in range(57, 59):
                if my_list[i] * my_list[j] == my_list[k]:
                    gcf = my_list[i] * my_list[j]
    return gcf
