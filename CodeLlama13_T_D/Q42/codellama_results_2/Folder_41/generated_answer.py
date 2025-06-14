
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()
    p = numbers[84]
    s = set([1])
    for i in range(2, int(p**0.5) + 1):
        while p % i == 0:
            s.add(i)
            p //= i
    if p > 1:
        s.add(p)
    return s
