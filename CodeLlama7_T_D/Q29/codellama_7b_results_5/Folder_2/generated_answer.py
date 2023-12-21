
def gcf_two_nums(my_list):
    gcf = 1
    for i in range(372, 752 + 1):
        if my_list[i] % gcf == 0 and my_list[i + 1] % gcf == 0:
            gcf = my_list[i]
    return gcf
