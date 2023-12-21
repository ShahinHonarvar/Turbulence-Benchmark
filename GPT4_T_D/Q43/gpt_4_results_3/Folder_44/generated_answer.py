
def find_primes_between_indices(int_list):
    primes = []
    for i in range(19, 86):
        if i < len(int_list):
            num = int_list[i]
            if num > 1:
                for j in range(2, num):
                    if (num % j) == 0:
                        break
                else:
                    primes.append(num)
    return sorted(primes, reverse=True)
