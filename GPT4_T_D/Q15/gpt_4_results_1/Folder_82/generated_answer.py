
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(20, min(201, len(int_list))):
        if int_list[i] % 2 == 1:
            odd_sum += int_list[i]
    return odd_sum
