def all_right_truncatable_prime(n):
    return sorted((i for i in range(2, n[0] + 1) if all(j == '9' or j == '0' for j in str(i)) and all(int(j) == 9 or int(j) == 0 for j in str(i))))
