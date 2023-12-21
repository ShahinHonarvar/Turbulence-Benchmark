
def all_right_truncatable_prime(nums):
    x = nums[74]
    prime_numbers = []
    
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if (n % i) == 0:
                return False
        return True

    def is_right_truncatable_prime(prime):
        prime = str(prime)
        while len(prime) > 0:
            if not is_prime(int(prime)):
                return False
            prime = prime[:-1]
        return True

    for num in range(1, x):
        if is_prime(num) and is_right_truncatable_prime(num):
            prime_numbers.append(num)
    
    return sorted(prime_numbers)
