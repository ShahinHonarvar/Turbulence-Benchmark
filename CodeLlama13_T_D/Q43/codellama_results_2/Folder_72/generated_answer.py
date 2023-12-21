
def find_primes_between_indices(numbers):
    prime_nums = []
    for num in numbers[28:45]:
        if is_prime(num):
            prime_nums.append(num)
    return sorted(prime_nums)
