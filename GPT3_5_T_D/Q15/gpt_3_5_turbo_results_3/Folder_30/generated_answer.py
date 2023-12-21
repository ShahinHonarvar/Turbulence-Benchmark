
def sum_odd_ints_inclusive(integers):
    sum = 0
    for i in range(55, 99):
        if i % 2 != 0:
            sum += integers[i]
    return sum
