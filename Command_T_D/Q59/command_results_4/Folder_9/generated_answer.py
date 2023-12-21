def all_left_truncatable_prime(x):
    # create a list of all the primes less than the given number
    primes = []
    # create a variable to store the number being tested
    num = 2
    # loop until the number is equal to the given number
    while num <= x:
        # if the number is prime, add it to the list of primes
        if all(num % i for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
        # move to the next number
        num += 1
    # return the list of primes
    return sorted(set(primes))
