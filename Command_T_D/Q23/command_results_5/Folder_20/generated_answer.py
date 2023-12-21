def find_divisors_in_range(x):
    divs = []
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            divs += [i]
            if i * i != x:
                divs += [x // i]
    return sorted(set(divs))
