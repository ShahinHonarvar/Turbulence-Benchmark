
def sum_in_range(int_list):
    sum_val = 0
    for num in int_list:
        if -8 <= num <= 8:
            sum_val += num
    return sum_val
