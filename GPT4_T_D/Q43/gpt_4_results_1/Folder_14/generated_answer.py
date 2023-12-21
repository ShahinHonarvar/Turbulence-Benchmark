
def find_primes_between_indices(numbers):
    primes = []
    for i in range(10, min(67, len(numbers))):
        number = numbers[i]
        if number > 1:
            for j in range(2, number):
                if (number % j) == 0:
                    break
            else:
                primes.append(number)

    return sorted(primes)
