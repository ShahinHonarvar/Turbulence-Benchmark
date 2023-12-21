
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[32]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            number_str = str(num)
            right_truncatable = True
            for i in range(len(number_str)-1):
                number_str = number_str[:-1]
                if not is_prime(int(number_str)):
                    right_truncatable = False
                    break
            if right_truncatable:
                primes.append(num)
    return sorted(primes)
