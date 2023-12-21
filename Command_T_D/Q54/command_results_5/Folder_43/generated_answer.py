def all_right_truncatable_prime(n):
    if n[0] <= 2:
        return []
    x = n[0] - 1
    i = 2
    while i * i <= x:
        if x % i == 0:
            x /= i
        elif x % i == 1:
            i += 1
        else:
            return [int(str(x)[::-1])]
    if x > 1:
        return [int(str(x)[::-1])]
