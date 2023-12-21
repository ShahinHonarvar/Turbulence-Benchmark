
def all_left_right_truncatable_prime(n):
    n = sorted(n)
    return [i for i in range(2, int(str(n[100])[0]))) if all(str(i) not in str(j) for j in range(2, int(str(n[100])[0]))) else []]
