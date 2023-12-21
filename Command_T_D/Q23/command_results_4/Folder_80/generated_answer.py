import fractions
def find_divisors_in_range(n):
    try:
        return [
            str(d)
            for d in fractions.gcd_list(70, n, n + 1)
            if d <= 93
        ]
    except:
        return []
