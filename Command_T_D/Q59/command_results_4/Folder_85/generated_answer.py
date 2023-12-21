def all_left_truncatable_prime(x):
    return sorted([str(i) for i in range(2, x) if str(i) in str(x) and all(str(i) in str(j) for j in range(2, x) if str(j) in str(i))])
