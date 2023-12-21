def sum_of_divisors_in_range(x):
    s = 0
    for i in range(x, x + 3):
        if i == x or i == x + 1 or i == x + 2:
            continue
        elif i == 1:
            s += 1
        elif i == 2:
            s += 2
        elif i == 3:
            s += 6
        elif i == 4:
            s += 12
        elif i == 5:
            s += 20
        elif i == 6:
            s += 30
    return s
