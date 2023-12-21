
def sum_odd_ints_inclusive(integer_list):
    total = 0
    for idx in range(28, 33):
        if len(integer_list) > idx and integer_list[idx] % 2 != 0:
            total += integer_list[idx]
    return total
