
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[126]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            num_str = str(i)
            if '0' in num_str:
                continue
            left_truncatable = True
            right_truncatable = True
            for j in range(1, len(num_str)):
                left_num = int(num_str[j:])
                right_num = int(num_str[:j])
                if not is_prime(left_num):
                    left_truncatable = False
                    break
                if not is_prime(right_num):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
