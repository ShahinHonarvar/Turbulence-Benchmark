def if_decimal_is_divisible(s):
    return if_sum_divisible(sum(int(i) for i in reversed(s)))
