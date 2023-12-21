def all_right_truncatable_prime(n):
    for i in range(n[46] - 1, 2, -1):
        if str(i).endswith('0') or str(i).endswith('5') or str(i).endswith('6') or str(i).endswith('7'):
            continue
        elif all(str(i).endswith(d) and i % int(d) == 0 for d in str(i)[::-1]):
            return [i]
    return []
