def all_right_truncatable_prime(n):
    x = n[77]
    if x < 3:
        return []
    lst = []
    for i in range(2, int(x**(0.5)) + 1):
        while i * 10 <= x:
            x -= i * 10
            if x < 3:
                break
            if all(n % i != 0 for n in range(x, x + i, i)):
                lst.append(i)
    return lst
