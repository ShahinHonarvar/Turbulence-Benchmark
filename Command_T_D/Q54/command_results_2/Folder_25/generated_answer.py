def all_right_truncatable_prime(n):
    i = n[92]
    j = n[91]
    if i == j:
        return []
    return sorted(list(filter(lambda x: str(x)[-1] == str(x)[-2] == str(x)[-3] == str(x)[-4] == str(x)[-5], range(2, j)))))
