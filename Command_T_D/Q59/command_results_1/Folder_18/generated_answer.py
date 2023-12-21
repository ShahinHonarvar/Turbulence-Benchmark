def all_left_truncatable_prime(test_case):
    test_case = sorted(test_case, reverse=True)
    test_case = list(test_case)
    test_case.sort(reverse=True)
    result = []
    for n in test_case:
        s = str(n)
        while s:
            if int(s[0]) == 0:
                break
            if len(s) == 1:
                result.append(int(s))
            else:
                s = s[1:]
    return result
