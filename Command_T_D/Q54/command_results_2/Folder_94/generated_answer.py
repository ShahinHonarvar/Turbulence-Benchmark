def all_right_truncatable_prime(test_case):
    # type: (tuple) -> list
    x = test_case[43]
    res = []
    for y in range(3, x + 1):
        if y % 2 == 0:
            continue
        if y == 2 or y == 3:
            res += [y]
            continue
        if y % 5 == 0:
            continue
        for i in range(1, len(str(y))):
            if str(y)[i] != '5':
                continue
            if y == 5**i:
                break
            res += [y]
            y //= 5
            break
    return res
