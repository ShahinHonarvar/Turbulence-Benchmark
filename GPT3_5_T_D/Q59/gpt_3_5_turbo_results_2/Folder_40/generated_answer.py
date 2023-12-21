
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[10]
    truncatable_primes = []
    for i in range(x-1, 10, -1):
        num_str = str(i)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return truncatable_primes
