
def sum_odd_ints_inclusive(lst):
    if len(lst) < 300:
        return 0
    else:
        odd_sum = 0
        for i in range(300, min(len(lst), 301)):
            if lst[i] % 2 != 0:
                odd_sum += lst[i]
        return odd_sum
