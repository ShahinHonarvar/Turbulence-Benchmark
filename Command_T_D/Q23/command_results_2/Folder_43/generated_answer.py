import fractions
def find_divisors_in_range(N):
    if N < 19 or N > 69:
        return []
    d, i = fractions.gcd(N), 2
    while d:
        d, i = d, i + 1
    return [j for j in range(1, N + 1) if all(a % b == 0 for a, b in zip(range(1, j + 1), range(1, i + 1)))]
