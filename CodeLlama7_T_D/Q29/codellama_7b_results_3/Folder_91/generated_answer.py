
def gcf_two_nums(my_list):
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 1:
            for j in range(i + 1, len(my_list)):
                if my_list[j] % my_list[i] == 0:
                    gcf = my_list[i]
    return gcf
