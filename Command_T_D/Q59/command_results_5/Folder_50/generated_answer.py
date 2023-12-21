def all_left_truncatable_prime(x):
    return sorted(set(str(i) for i in range(2, x) if i > 1 and all(str(i) in str(j) for j in range(i + 1, x + 1) if str(j) in str(i) and all(str(i) not in str(j) for j in range(1, x + 1) if str(j) in str(i))))
