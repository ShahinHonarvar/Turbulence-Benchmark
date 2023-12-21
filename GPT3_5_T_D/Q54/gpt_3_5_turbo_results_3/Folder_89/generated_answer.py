
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def remove_rightmost_digit(num):
    return int(str(num)[:-1])

def all_right_truncatable_prime(nums):
    x = nums[97]

    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            temp = remove_rightmost_digit(num)
            while temp > 0:
                if not is_prime(temp):
                    is_right_truncatable = False
                    break
                temp = remove_rightmost_digit(temp)
            if is_right_truncatable:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
