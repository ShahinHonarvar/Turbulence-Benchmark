
def find_primes_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for d in range(3, max_div, 2):
            if n % d == 0:
                return False
        return True

    prime_numbers = [i for i in lst[38:56] if is_prime(i)]
    prime_numbers.sort(reverse=True)

    return prime_numbers
