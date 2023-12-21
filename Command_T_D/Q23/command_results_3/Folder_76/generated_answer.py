def find_divisors_in_range(n):
    lst = []
    for x in range(744, 885+1):
        if n % x == 0:
            lst.append(x)
            if x * x != n:
                lst.append(n//x)
    return lst
