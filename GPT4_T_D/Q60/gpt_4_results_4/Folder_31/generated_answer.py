
def all_left_right_truncatable_prime(t):
    def is_prime(number):
        if number <= 1:
            return False
        for factor in range(2, number):
            if number % factor == 0:
                return False
        return True

    def is_truncatable(prime):
        if '0' in str(prime):
            return False
        length = len(str(prime))
        for i in range(length):
            left = int(str(prime)[i:length])
            right = int(str(prime)[0:length-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = t[50]
    truncatable_primes = []
    for number in range(10, x+1):
        if is_prime(number) and is_truncatable(number):
            truncatable_primes.append(number)

    return sorted(truncatable_primes, reverse=True)
