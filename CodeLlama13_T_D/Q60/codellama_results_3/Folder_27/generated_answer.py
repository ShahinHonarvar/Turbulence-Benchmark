
def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(num):
    # Check if the number contains 0
    if '0' in str(num):
        return False

    # Check if the number is prime
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    # Check if the number remains prime when leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, int(math.log10(num)) + 1):
        num_left = num // (10 ** i)
        num_right = num % (10 ** i)
        if not is_prime(num_left) or not is_prime(num_right):
            return False

    return True

def is_prime(num):
    # Check if the number is prime
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
