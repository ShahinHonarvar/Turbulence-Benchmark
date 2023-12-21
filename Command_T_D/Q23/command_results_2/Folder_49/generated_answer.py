def find_divisors_in_range(x):
    divs = []
    for i in range(2, x // 2):
        if x % i == 0:
            divs.append(i)
            if i * i != x:
                divs.append(x // i)
    if x % 2 == 0:
        divs.append(2)
    return divs
