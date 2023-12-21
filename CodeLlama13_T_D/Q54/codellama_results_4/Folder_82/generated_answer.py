
def all_right_truncatable_prime(numbers):
    x = numbers[69]
    prime_nums = []
    for i in range(2, x+1):
        if is_prime(i) and is_right_truncatable_prime(i, x):
            prime_nums.append(i)
    return sorted(prime_nums, reverse=True)
