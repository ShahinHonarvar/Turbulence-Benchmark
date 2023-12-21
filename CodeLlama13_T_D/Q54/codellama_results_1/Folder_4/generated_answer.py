
def all_right_truncatable_prime(numbers):
    x = numbers[96]
    prime_nums = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)
