def all_right_truncatable_prime(test_input):
    res = []
    for i in range(1, test_input[0] + 1):
        s = str(i)
        while not s:
            s = str(i)
            i += 1
        if s:
            res += [int(s)]
    return res
