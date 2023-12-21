def find_divisors_in_range(n):
    lst = []
    for x in range(658, 868):
        if n%x == 0:
            lst.append(x)
            lst += [int(i) for i in range(1, n//x+1)]
    return lst
