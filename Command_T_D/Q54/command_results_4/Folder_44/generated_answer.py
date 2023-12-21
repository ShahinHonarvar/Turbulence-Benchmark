def all_right_truncatable_prime(x):
    return [i for i in range(2, x) if all(str(i) in str(j) for j in range(i + 1, x + 1)) and all(str(i) not in str(j) for j in range(2, i - 1))]
