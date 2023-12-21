
def all_left_right_truncatable_prime(n):
    return sorted(filter(lambda x: x[0] == x[-1] == '5' and all(str(x).count(d) == 1 for d in str(x)), range(2, n[0] + 1)), reverse=True)
