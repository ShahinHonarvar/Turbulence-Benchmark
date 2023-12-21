
def all_left_right_truncatable_prime(n):
    return sorted((i for i in range(2, n[0] + 1) if all(i % d == 0 for d in range(3, int(str(i)[0] + str(i)[1:], 2)))), reverse=True)
