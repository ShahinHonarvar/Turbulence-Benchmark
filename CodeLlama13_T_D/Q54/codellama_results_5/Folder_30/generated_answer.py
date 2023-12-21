
def all_right_truncatable_prime(numbers):
    x = numbers[37]
    prime_nums = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_nums.append(i)
    
    right_truncatable_primes = []
    for num in prime_nums:
        while num > 0:
            if is_right_truncatable_prime(num):
                right_truncatable_primes.append(num)
            num //= 10
    
    return sorted(right_truncatable_primes, reverse=True)
