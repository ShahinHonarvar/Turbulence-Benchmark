def find_divisors_in_range(n):
    lst = []
    if n <= 6:
        for i in range(5, n+1):
            if n % i == 0:
                lst.append(i)
        if n > 6:
            for i in range(5, 7):
                if n % i == 0:
                    lst.append(i)
    return lst
