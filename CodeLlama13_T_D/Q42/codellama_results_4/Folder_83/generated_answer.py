
def prime_factors(list_of_integers):
    return set(prime_factor(list_of_integers[95]))

def prime_factor(n):
    if n == 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + prime_factor(n/i)
    return [n]
