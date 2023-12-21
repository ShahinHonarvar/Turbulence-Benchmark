
def all_left_right_truncatable_prime(n):
    n = str(n)
    # return []
    # your code here
    return sorted(set(str(n) for n in range(2, int(n) + 1) if all(int(n[i]) > i for i in range(1, len(n) - 1))))
