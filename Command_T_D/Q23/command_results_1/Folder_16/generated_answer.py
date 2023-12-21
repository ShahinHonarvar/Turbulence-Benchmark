def find_divisors_in_range(x):
    # Your code here
    res = []
    for i in range(228, 846):
        if x % i == 0:
            res.append(i)
            if x != i * i:
                res.append(x // i)
    return res
