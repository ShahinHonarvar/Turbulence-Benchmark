def all_right_truncatable_prime(n):
    return [i for i in range(2, int(n[30]) + 1) if all(str(i) in str(j) for j in range(i + 1, int(n[30]) + 1) if str(j) in str(i) and all(str(i) in str(j) for j in range(i + 1, int(n[30]) + 1) if str(j) in str(i)))
