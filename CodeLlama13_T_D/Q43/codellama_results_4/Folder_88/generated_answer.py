
def find_primes_between_indices(nums):
    prime_list = []
    for i in range(66, 81):
        if nums[i] not in prime_list:
            if is_prime(nums[i]):
                prime_list.append(nums[i])
    return sorted(prime_list)
