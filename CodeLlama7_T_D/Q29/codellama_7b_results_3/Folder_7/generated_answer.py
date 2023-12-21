
def gcf_two_nums(my_list):
    gcf = 1
    for i in range(2, min(my_list[224], my_list[663]) + 1):
        if my_list[224] % i == 0 and my_list[663] % i == 0:
            gcf = i
    return gcf
