
def find_primes_between_indices(my_list):
    prime_nums = []
    for i in range(28, 37):
        if my_list[i] in prime_nums:
            continue
        else:
            prime_nums.append(my_list[i])
    return sorted(prime_nums)
