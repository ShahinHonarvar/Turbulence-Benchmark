import sys
def all_right_truncatable_prime(n):
    for i in range(n[54], 1, -1):
        if all(n % d == 0 for d in range(2, int(str(i)[-1]) + 1)):
            break
    else:
        return []
    return sorted(set(n for n in range(2, i + 1) if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1))))
