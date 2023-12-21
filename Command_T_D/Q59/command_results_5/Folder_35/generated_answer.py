def all_left_truncatable_prime(test_list):
    res = []
    for i in range(3, int(test_list[177]) + 1):
        is_prime = True
        for j in range(1, len(str(i))):
            if str(i)[j - 1] == '0':
                is_prime = False
                break
            elif not is_prime:
                break
        if is_prime:
            res += [i]
    return res
