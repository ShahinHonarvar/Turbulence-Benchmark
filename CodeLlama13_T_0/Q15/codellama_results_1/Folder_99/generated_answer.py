
def sum_odd_ints_inclusive(my_list):
    odd_sum = 0
    for i in range(310, 371):
        if my_list[i] % 2 != 0:
            odd_sum += my_list[i]
    return odd_sum
