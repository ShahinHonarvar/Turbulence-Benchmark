
def all_right_truncatable_prime(numbers):
    x = numbers[7]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    right_truncatable_primes = []
    for number in range(2, x):
        if is_right_truncatable_prime(number):
            right_truncatable_primes.append(number)
            
    return sorted(right_truncatable_primes)
