
def find_divisors_in_range(n):
    res = []
    for i in range(5, 10):
        if n % i == 0:
            res.append(i)
    return res
