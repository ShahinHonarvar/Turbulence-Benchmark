
def all_left_right_truncatable_prime(nums):
    x = nums[466]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if all(int(str_prime[j:i+1])%k!=0 for k in range(2, int(int(str_prime[j:i+1])**0.5)+1)) and all(int(str_prime[i:j+1])%k!=0 for k in range(2, int(int(str_prime[i:j+1])**0.5)+1)):
                if i == len(str_prime) - 1:
                    truncatable_primes.append(prime)
            else:
                break
    return sorted(truncatable_primes, reverse=True)
