
def gcf_two_nums(my_list):
    gcf = 1
    for i in range(min(my_list[372], my_list[752])):
        if my_list[372] % i == 0 and my_list[752] % i == 0:
            gcf = i
    return gcf
