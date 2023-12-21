def all_right_truncatable_prime(num_tup):
    res = []
    for i in range(num_tup[0], num_tup[1]):
        if all(n % d == 0 for d in range(2, int(str(n)[-1]))) and all(n == int(str(n)[-1]) for n in range(2, i)):
            res.append(i)
    return res
