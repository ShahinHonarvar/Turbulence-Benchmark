
def find_primes_between_indices(numbers):
    primes = []
    for i in range(66, 82):
        if i < len(numbers):
            num = numbers[i]
            if num > 1:
                for j in range(2, num):
                    if (num % j) == 0:
                        break
                else:
                    primes.append(num)
    return sorted(primes)
