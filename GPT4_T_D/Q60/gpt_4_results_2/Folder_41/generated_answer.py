
def all_left_right_truncatable_prime(numbers):
    x = numbers[46]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n)-i])):
                return False
        return True

    truncatable_primes = [i for i in range(10, x+1) if is_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
