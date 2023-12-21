
def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[23:49]:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return sorted(prime_nums)
