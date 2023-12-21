def all_right_truncatable_prime(n):
    x = n[65]
    return sorted(filter(lambda a: str(a).endswith("9") and str(a)[-2] != "0" and all(str(a)[i] != "0" for i in range(1, len(str(a)))), range(2, x + 1)), reverse=True)
