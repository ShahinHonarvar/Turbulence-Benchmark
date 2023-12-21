
def find_primes_between_indices(my_list):
    start, end = 29, 97
    prime_nums = []
    for i in range(start, end+1):
        if is_prime(i) and my_list[i] not in prime_nums:
            prime_nums.append(my_list[i])
    return sorted(prime_nums, reverse=True)
