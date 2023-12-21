def all_right_truncatable_prime(n):
    if n[26] < 2:
        return []
    s = str(n[26])
    return sorted([int(s[0] + s[1:3] + s[4:]) for i in range(len(s) - 3) if all(str(2 * i + 1)[-1] not in str(j) for j in range(2, int(s[0] + s[1:3] + s[4:])))])
