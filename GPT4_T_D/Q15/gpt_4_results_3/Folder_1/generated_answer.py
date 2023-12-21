
def sum_odd_ints_inclusive(int_list):
    odd_sum = 0
    for i in range(31, 73):
        try:
            if int_list[i] % 2 != 0:
                odd_sum += int_list[i]
        except IndexError:
            break
    return odd_sum
