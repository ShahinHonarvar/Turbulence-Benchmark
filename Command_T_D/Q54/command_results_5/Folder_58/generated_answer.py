def all_right_truncatable_prime(n):
    for i in range(2, n[0]):
        if all(str(j) in str(i) for j in range(2, int(str(i)[-1]) + 1)):
            yield i
    return []
