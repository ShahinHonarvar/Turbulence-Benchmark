
def sum_odd_ints_inclusive(integers):
    sum_odd = 0
    for i in range(527, 539):
        if i < len(integers) and integers[i] % 2 != 0:
            sum_odd += integers[i]
    return sum_odd
