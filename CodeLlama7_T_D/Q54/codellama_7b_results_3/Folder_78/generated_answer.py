
def all_right_truncatable_prime(nums):
    # Get the last rightmost digit of each number
    digits = [int(str(n)[-1])) for n in nums]
    # Find the prime numbers with the same last rightmost digit as the original number
    prime_digits = []
    for i, d in enumerate(digits):
        if is_prime(nums[i] // 10**(len(str(nums[i])) - 1)) and nums[i] % d == 0:
            prime_digits.append(d)
    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted(prime_digits)
