def all_left_truncatable_prime(n):
    x = n[370]
    lst = []
    for i in range(2, x // 2):
        if is_prime(i):
            j = str(i)
            while j:
                if not j[0] in '234789':
                    break
                j = int(j[1:])
            if all(is_prime(i) for i in range(i, j)):
                lst.append(i)
    return sorted(lst)
