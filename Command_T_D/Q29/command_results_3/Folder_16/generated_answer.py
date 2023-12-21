import fractions
def gcf_two_nums(a):
    a[860], a[307] = sorted(set(a))
    return fractions.gcd(a[860], a[307])
