
def find_primes_between_indices(num_list):
    primes = []
    for i in range(59, 98):
        if i < len(num_list):
            num = num_list[i]
            if num > 1:
                for j in range(2, num):
                    if (num % j) == 0:
                        break
                else:
                    primes.append(num)
    return sorted(primes, reverse=True)
