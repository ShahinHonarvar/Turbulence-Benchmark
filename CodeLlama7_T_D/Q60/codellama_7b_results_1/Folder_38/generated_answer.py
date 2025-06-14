 def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if n has no 0 digits
    if '0' in str(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(2, len(str(n)))):
        num = n
        while True:
            num = int(str(num)[:i] + str(num)[i+1:]))
            if is_prime(num):
                return True

            else:
                break

    # If the above conditions are not met, then n is not a left-and-right-truncatable prime number
    return False

def is_prime(n):

    # Check if n is an integer

    if not isinstance(n, int):
        return False

    # Check if n is greater than 1

    if n <= 1:
        return False

    # Check if n has no factors other than 1 and itself

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the above conditions are met, then n is prime

    return True
