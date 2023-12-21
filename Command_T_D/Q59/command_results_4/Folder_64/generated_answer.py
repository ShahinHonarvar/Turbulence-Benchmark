def all_left_truncatable_prime(n):
    return sorted(set(str(i) for i in range(2, n[4]) if all(int(d) for d in str(i) if d!='0')))
