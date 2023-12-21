import re
def all_left_truncatable_prime(n):
    a = n[0]
    for i in range(2, int(str(n[0])[0]) + 1):
        if str(a).count(str(i)) > 1:
            break
        a -= i
    for j in range(2, int(str(a))[0] + 1):
        if str(a).count(str(j)) > 1:
            break
        a -= j
    return sorted(set(range(a, n[1] + 1)), reverse=True)
