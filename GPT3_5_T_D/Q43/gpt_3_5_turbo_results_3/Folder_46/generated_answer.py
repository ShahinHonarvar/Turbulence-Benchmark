
def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[20:26]:
        if num > 1:
            is_prime = True
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    
    primes.sort(reverse=True)
    return primes
