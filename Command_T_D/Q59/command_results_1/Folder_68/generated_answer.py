import re
def all_left_truncatable_prime(n):
    l = []
    for i in range(2, n[0] + 1):
        while left_re.match(str(i)):
            i = int(left_re.sub(r'\1', str(i), str(i)))
        if i > 1 and all(i % d for d in range(3, int(str(i)[-1]))) and i not in l:
            l.append(i)
    return sorted(set(l), reverse=True)
