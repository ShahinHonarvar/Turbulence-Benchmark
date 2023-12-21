
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            num_str = str(num)
            if '0' in num_str:
                continue
            while len(num_str) > 2:
                if not is_prime(int(num_str[1:-1])):
                    break
                num_str = num_str[:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
