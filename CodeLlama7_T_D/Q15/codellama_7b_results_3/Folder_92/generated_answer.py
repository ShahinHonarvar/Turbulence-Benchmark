 def sum_odd_ints_inclusive(my_list):
    odd_int_sum = 0
    for i in range(1, len(my_list)):
        if my_list[i] % 2 != 0:
            odd_int_sum += my_list[i]
    return odd_int_sum
