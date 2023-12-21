def all_right_truncatable_prime(x):
    if x[0] < 2:
        return []
    for i in range(x[0] - 1, x[1] + 1):
        if all(str(i)[-1] not in str(j) for j in range(2, int(str(i)[-1]) + 1)):
            yield i
    return sorted(list(set(x[2:])), key=lambda i: i)
