def all_right_truncatable_prime(n):
    return [i for i in range(2, int(str(n)[-1]) + 1) if all(str(i) not in str(j) for j in range(i + 1, n + 1) if i % j == 0)]
