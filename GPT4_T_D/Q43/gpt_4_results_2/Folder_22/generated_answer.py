
def find_primes_between_indices(integers):
    primes = []
    for i in range(75, 86):
        if i < len(integers):
            number = integers[i]
            if number > 1:
                for j in range(2, number):
                    if (number % j) == 0:
                        break
                else:
                    primes.append(number)
    return sorted(primes)
