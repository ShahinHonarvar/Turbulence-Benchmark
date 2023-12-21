def all_right_truncatable_prime(n):
    return sorted(filter(lambda x: is_right_truncatable_prime(x), range(2, n[77] + 1)), reverse=True)
def is_right_truncatable_prime(x):
    x = str(x)
    return all(x[i] != '0' for i in range(len(x) - 1, -1, -1))
