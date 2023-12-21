
def find_sum_of_multiples(n):
    res = 0
    for i in range(1, 38):
        res += n * i
    return res
