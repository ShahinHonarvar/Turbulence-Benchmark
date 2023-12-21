def all_right_truncatable_prime(n):
    return [p for p in range(2, n[0] + 1) if all(p % d for d in range(2, int(str(p)[-1]))) and all(str(p)[-1] not in str(q) for q in range(2, int(str(p)[-1]))) and all(str(p)[-1] not in str(q) for q in range(2, int(str(p)[-1]))) and str(p)[-1] not in str(q) for q in range(2, int(str(p)[-1])))
