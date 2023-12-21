def all_right_truncatable_prime(test_list):
    res = []
    for n in range(2, test_list[93]):
        is_prime = True
        for d in range(2, int(str(n)[-1]) + 1):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            res.append(n)
    return res
