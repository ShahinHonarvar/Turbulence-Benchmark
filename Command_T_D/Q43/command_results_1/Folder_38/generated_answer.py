def find_primes_between_indices(list):
    start = 55
    end = 87
    primes = []
    for num in range(start, end+1):
        is_prime = True
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
