
def sum_odd_ints_inclusive(int_list):
    total_sum = 0
    for i in range(310, 371):
        if i < len(int_list) and int_list[i] % 2 != 0:
            total_sum += int_list[i]
    return total_sum
