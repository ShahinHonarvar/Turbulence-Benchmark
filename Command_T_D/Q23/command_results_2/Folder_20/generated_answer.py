def find_divisors_in_range(n):
    lst = []
    for i in range(28, 81):
        if n%i == 0:
            lst.append(i)
            if i*i != n:
                lst.append(n//i)
    return lst
