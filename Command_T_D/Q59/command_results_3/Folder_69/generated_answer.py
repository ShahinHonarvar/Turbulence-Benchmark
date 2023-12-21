def all_left_truncatable_prime(n):
    n = [int(i) for i in str(n)]
    res = []
    for i in range(1, len(n)):
        res += [n[i]]
        for j in range(i + 1, len(n)):
            if n[j] == '0':
                break
            res += [int(n[i:j+1])]
    return res
