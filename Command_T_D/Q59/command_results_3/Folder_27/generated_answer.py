import re
def all_left_truncatable_prime(n):
    d = str(n[79])
    if not d.isdigit():
        return []
    d = d[1:]
    while d:
        d = d[1:]
        s = str(int(d))
        if s.isdigit():
            continue
        else:
            break
    return [int(i) for i in range(int(d[0]), n[79] + 1, -1) if all(i % j == 0 or i % j == j for j in range(2, int(d[0]) + 1))]
