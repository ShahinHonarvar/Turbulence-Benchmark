
def all_right_truncatable_prime(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def right_truncatable_prime(n):

    s = str(n)

    for i in range(len(s)-1, -1, -1):

        if not is_prime(int(s[:i] + s[i+1:])):

            return False


    return True
