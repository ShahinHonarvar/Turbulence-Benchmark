
def all_left_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_truncatable_prime(num):
    if num < 2 or not str(num).isdigit():
        return False
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[i:])):
            return False
    return True

def is_prime(num):
    if num < 2 or not str(num).isdigit():
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
