
def sum_odd_ints_inclusive(integers):
    sum = 0
    for i in range(42, 69):
        if i < len(integers) and integers[i] % 2 != 0:
            sum += integers[i]
    return sum
