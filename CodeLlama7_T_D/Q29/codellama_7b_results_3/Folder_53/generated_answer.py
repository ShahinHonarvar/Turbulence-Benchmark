
def gcf_two_nums(my_list):
    gcf = 1
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] % my_list[j] == 0 and my_list[j] > gcf:
                gcf = my_list[j]
    return gcf
