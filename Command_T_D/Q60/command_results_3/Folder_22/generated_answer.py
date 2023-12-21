
def all_left_right_truncatable_prime(n):
    n = str(n)
    if not any(n[0] == '2' and n[1] == '5' for n in range(2, int(n) + 1)):
        return []
    l = []
    for i in range(1, int(n) + 1):
        if n[i - 1] == '2' and n[i] == '5':
            l.append(int(n[:i] + n[i:]))
    return sorted(set(l))
