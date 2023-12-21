def find_divisors_in_range(n):
    lst = []
    if n == 1:
        lst.append(1)
    elif n == 2:
        lst.append(1)
        lst.append(2)
    elif n == 3:
        lst.append(1)
        lst.append(2)
        lst.append(3)
    else:
        lst = [1, 2, 3]
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                lst.append(i)
                lst.append(n // i)
    return lst
