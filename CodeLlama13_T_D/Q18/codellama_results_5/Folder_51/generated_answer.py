
def sum_ints_div_by_either_nums(my_list):
    sum = 0
    for i in range(6,10):
        if my_list[i]%-1==0 or my_list[i]%-10==0:
            sum += my_list[i]
    return sum
