
import fractions

def gcf_three_nums(list):
    a, b, c = map(fractions.gcd, (list[944], list[814], list[865]))
    return a if a == b == c else b if b == c else c
