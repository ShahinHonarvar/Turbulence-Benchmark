def all_right_truncatable_prime(n):
    if not n:
        return []
    lst = []
    lst += [str(x) for x in range(2, n[0]) if all(x % y == 0 for y in range(2, int(str(x))[0] + 1)]]
    lst += [str(x) for x in range(3, n[0] + 1) if all(x % y == 0 for y in range(3, int(str(x))[0] + 1)]]
    return sorted(set(lst), reverse=True)
