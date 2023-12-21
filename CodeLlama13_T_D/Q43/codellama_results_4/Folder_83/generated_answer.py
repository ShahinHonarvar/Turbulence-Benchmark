
def find_primes_between_indices(my_list):
    prime_nums = []
    for num in my_list:
        if is_prime(num) and 14 <= num <= 73:
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)
