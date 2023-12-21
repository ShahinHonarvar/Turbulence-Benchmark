
def find_primes_between_indices(numbers):
    primes = []
    for i in range(20, 26):
        if i < len(numbers):
            number = numbers[i]
            if number > 1:
                for j in range(2, number):
                    if (number % j) == 0:
                        break
                else:
                    primes.append(number)
    primes.sort(reverse=True)
    return primes
