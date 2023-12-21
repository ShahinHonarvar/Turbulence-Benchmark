
def sum_odd_ints_inclusive(int_list):
    sum_val = 0
    for i in range(5, 8):
        if int_list[i] % 2 != 0:
            sum_val += int_list[i]   
    return sum_val
