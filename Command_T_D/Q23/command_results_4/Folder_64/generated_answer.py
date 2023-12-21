def find_divisors_in_range(n):
    lst = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == n:
                lst.append(i)
                lst.append(j)
                break
    return lst
