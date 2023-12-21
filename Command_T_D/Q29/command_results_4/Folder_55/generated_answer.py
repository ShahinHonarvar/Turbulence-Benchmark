import fractions
def gcf_two_nums(lst):
    dct = {}
    for n in lst:
        dct[n] = dct[n] + 1
    return fractions.gcd(dct[lst[0]]//2, dct[lst[1]]//2)
