
def sum_odd_ints_inclusive(int_list):
    total = 0
    for i in int_list[686:988]:
        if i % 2 != 0:
            total += i
    return total
