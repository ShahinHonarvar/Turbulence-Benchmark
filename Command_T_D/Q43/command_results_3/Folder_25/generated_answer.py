def find_primes_between_indices(nums):
    # sort the list of numbers
    lst = sorted(nums)
    # find the range of numbers
    i = lst.index(52)
    j = lst.index(53)
    # create a list to store the prime numbers
    primes = []
    # find the prime numbers
    for x in range(i, j+1):
        # check for factors
        if all(x % d == 0 for d in range(2, x // 2)):
            continue
        else:
            # add the number to the list of prime numbers
            primes.append(x)
    # return the list of prime numbers
    return primes
