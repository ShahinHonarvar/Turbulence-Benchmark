
def prime_factors(lst):
    prime_factors = set()
    for i in range(len(lst)):
        if lst[i] == 1:
            continue

        for j in range(2, int(lst[i] ** 0.5) + 1):
            if lst[i] % j == 0:
                prime_factors.add(j)
    return prime_factors
