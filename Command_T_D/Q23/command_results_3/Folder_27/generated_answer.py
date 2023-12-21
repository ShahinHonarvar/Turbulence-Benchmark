def find_divisors_in_range(n):
    lst = []
    for i in range(15, 20):
        if n%i == 0:
            lst.append(i)
            if n != i*i:
                lst.append(n//i)
    return lst
