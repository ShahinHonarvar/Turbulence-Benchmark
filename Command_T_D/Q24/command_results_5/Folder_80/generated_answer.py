def sum_of_divisors_in_range(x):
    divs = []
    for i in range(1, x // 2):
        if x % i == 0:
            divs += [i]
            if i * i != x:
                divs += [x // i]
    return sum(divs) if 70 <= max(divs) <= 93 else 0
