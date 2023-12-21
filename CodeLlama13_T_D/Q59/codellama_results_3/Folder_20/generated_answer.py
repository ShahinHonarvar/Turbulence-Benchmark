
def all_left_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
