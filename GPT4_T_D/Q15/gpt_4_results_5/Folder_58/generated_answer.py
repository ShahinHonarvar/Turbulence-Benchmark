
def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in range(209, min(557, len(int_list))):
        if int_list[i] % 2 != 0:
            total += int_list[i]
    return total
