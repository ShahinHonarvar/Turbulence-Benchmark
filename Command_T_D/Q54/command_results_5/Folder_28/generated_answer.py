def all_right_truncatable_prime(test_case):
    try:
        return [
            int(str(x)[1:])
            for x in range(2, test_case[19] + 1)
            if all(x % d == 0 for d in range(3, int(str(x)[-1]) + 1, 2))
        ]
    except:
        return []
