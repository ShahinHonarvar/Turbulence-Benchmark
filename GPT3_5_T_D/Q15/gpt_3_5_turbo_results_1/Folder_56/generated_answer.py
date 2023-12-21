
def sum_odd_ints_inclusive(integers):
    odd_sum = 0
    for i in range(len(integers)):
        if i % 2 == 1:
            odd_sum += integers[i]
    return odd_sum
