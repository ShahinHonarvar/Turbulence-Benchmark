
def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[29:98]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return sorted(prime_nums, reverse=True)
