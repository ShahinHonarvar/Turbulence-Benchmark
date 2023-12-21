
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x):
        is_prime = True
        while is_prime:
            is_prime = all(str(i) not in str(j) for j in range(i + 1, i + 10))
            i += 1
            if is_prime:
                res.append(i)
    return res
