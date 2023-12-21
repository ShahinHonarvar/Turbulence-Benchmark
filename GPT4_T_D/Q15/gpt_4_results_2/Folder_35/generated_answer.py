
def sum_odd_ints_inclusive(int_list):
    total = 0
    for num in int_list[30:49]:
        if num % 2 != 0:
            total += num
    return total
