def all_right_truncatable_prime(lst):
    return [n for n in lst if all(n % d != 0 for d in range(2, int(str(n)[-1])))]
