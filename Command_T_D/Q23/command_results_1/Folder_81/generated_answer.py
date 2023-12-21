def find_divisors_in_range(n):
    if n <= 2:
        return []
    lst = []
    for i in range(3, n+1):
        if n%i == 0:
            lst.append(i)
            lst.append(n//i)
    return lst
