def all_right_truncatable_prime(test_list):
    res = []
    for x in test_list:
        y = x
        while y:
            if all(a == 0 for a in str(y)):
                break
            y //= 10
        else:
            break
        res += [y]
    return res
