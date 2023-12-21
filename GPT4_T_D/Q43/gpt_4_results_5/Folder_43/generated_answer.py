
def find_primes_between_indices(numbers):
    numbers = numbers[31:93]
    primes = []
    
    for number in numbers:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                primes.append(number)

    return sorted(primes, reverse=True)
