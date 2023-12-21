def find_divisors_in_range(n):
    if n < 615 or n > 792:
        return []
    else:
        l = []
        for i in range(1, int(n ** .5) + 1):
            if n % i == 0:
                l.append(i)
                l.append(n // i)
        return sorted(set(l))
