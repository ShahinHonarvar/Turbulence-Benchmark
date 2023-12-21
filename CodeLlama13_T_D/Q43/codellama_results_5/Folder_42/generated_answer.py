
def find_primes_between_indices(numbers):
    primes = []
    for i in range(30, 43+1):
        if numbers[i] == 2:
            primes.append(numbers[i])
        elif numbers[i] % 2 != 0 and numbers[i] > 2:
            is_prime = True
            for j in range(3, int(math.sqrt(numbers[i]))+1):
                if numbers[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(numbers[i])
    return sorted(primes)
