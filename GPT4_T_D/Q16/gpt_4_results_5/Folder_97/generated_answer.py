
def sum_even_ints_inclusive(int_list):
    sum_val = 0
    for i in range(40, 81):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_val += int_list[i]
    return sum_val
