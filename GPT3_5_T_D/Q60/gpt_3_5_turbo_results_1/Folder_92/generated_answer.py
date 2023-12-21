
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    truncatable_primes = []
    x = nums[7]

    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True

            for i in range(1, len(num_str) + 1):
                if int(num_str[:i]) not in truncatable_primes or int(num_str[i:]) not in truncatable_primes:
                    is_truncatable = False
                    break

            if is_truncatable:
                truncatable_primes.append(num)

    return truncatable_primes
