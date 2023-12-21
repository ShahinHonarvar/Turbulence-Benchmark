
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[77]
    primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            prime = str(num)
            truncated_prime = prime
            while truncated_prime != '':
                if not is_prime(int(truncated_prime)):
                    break
                truncated_prime = truncated_prime[:-1]
            else:
                primes.append(int(prime))
    primes.sort(reverse=True)
    return primes
