
def sum_odd_ints_inclusive(integers):
    odd_sum = sum(i for i in integers[14:65] if i % 2 != 0)
    return odd_sum if odd_sum else 0
