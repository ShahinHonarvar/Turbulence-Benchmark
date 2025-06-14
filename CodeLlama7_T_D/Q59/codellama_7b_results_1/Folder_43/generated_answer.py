 def all_left_truncatable_prime(tuple):
    x = tuple[89]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    string = str(n)

    for i in range(len(string)):
        if string[i] == "0":
            return False

    for i in range(len(string)):
        if string[i] != "1" and string[i] != "3" and string[i] != "7":
            return False

    return True
