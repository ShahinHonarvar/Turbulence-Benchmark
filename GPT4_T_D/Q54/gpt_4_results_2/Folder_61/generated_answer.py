
def all_right_truncatable_prime(numbers):
    x = numbers[3]
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**(0.5))+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        while len(n) > 0:
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True

    results = [i for i in range(x) if is_right_truncatable_prime(i)]
    results.sort(reverse=True)

    return results
