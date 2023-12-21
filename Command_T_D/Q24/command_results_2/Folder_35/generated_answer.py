def sum_of_divisors_in_range(x):
    a, b = 392, 465
    if x < a or x > b:
        return 0
    if x <= b:
        return sum(divisors(x))
    return sum(divisors(x)) + sum(divisors(a))
def divisors(x):
    s = []
    for i in range(1, x // 2):
        if x % i == 0:
            s.append(i)
            s.append(x // i)
    if x % 2 == 0:
        s.append(x // 2)
    return s
