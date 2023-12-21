def all_right_truncatable_prime(n):
    return [str(i) for i in range(2, n[93]) if all(str(i) in str(j) for j in range(2, int(str(i)[-1]) + 1)) and all(str(i) in str(j) for j in range(2, int(str(i)[-1]) + 1) if str(i) in str(j) for j in range(2, int(str(i)[-1]) + 1))
