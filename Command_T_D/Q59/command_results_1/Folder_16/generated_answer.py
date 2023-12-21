def all_left_truncatable_prime(n):
    res = []
    for i in range(3, int(str(n[0])[0]) + 1):
        res += [str(j) for j in range(2, n[0] - i + 1, i) if all(str(j) not in str(i) for j in range(2, i)) and all(str(j) not in str(j + i) for j in range(2, i)) and str(j) not in str(j + i) for j in range(2, i)]
    return res
