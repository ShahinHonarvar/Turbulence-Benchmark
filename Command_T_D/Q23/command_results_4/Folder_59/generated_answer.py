def find_divisors_in_range(n):
    lst = []
    if n > 4:
        for i in range(3, int(n ** .5) + 1):
            if n % i == 0:
                lst.append(i)
                if i * i != n:
                    lst.append(n // i)
    if n % 2 == 0:
        lst.append(2)
    if n % 3 == 0:
        lst.append(3)
    if n % 5 == 0:
        lst.append(5)
    return lst
