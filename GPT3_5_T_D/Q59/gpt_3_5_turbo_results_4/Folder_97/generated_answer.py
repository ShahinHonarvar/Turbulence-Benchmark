
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
   
    x = numbers[645]
    left_truncatable_primes = []
   
    def recursive_check(number):
        if number < 10:
            if is_prime(number):
                left_truncatable_primes.append(number)
            return
        if is_prime(number):
            left_truncatable_primes.append(number)
            for digit in range(1, 10):
                recursive_check(int(str(digit) + str(number)[:-1]))
   
    for digit in range(1, 10):
        recursive_check(int(str(digit) + str(x)[:-1]))
   
    return sorted(left_truncatable_primes)
