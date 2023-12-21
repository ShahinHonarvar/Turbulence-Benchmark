
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for x in nums:
        for i in range(2, x):
            if is_prime(i):
                str_i = str(i)
                if '0' in str_i:
                    continue
                truncatable = True
                for j in range(1, len(str_i)):
                    left_truncated = int(str_i[j:])
                    right_truncated = int(str_i[:-j])
                    if not is_prime(left_truncated) or not is_prime(right_truncated):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(i)
    return sorted(primes, reverse=True)
