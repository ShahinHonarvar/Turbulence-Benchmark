
def sum_odd_ints_inclusive(integers):
    sum = 0
    for i in range(75, 89):
        if integers[i] % 2 != 0:
            sum += integers[i]
    return sum
