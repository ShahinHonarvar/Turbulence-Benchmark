
def sum_odd_ints_inclusive(integers):
    total = 0
    for i in range(4):
        if (i < len(integers)) and (integers[i] % 2 != 0):
            total += integers[i]
    return total
