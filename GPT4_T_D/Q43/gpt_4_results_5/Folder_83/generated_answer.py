
def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[14:74]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)
