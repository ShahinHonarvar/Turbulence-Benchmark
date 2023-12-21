import itertools
def all_left_truncatable_prime(nums):
    # Filter the input to only get prime numbers.
    primes = [x for x in nums if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]
    # Create a list of pairs of numbers that differ by a single digit.
    # For example, this will create a pair for each of the following:
    #
    # 1) 99
    # 2) 99, 9900
    # 3) 99, 9900, 99000
    #
    # The key here is that the first element of each pair is a prime number
    # and the second element is a left-truncatable number.
    #
    # Since the list of primes is already sorted in ascending order,
    # we can pass it directly to `itertools.accumulate` to calculate
    # the list of pairs.
    pairs = itertools.accumulate(primes)
    # Now that we have the list of pairs, we can filter it to
    # only include pairs where the second element is left-truncatable.
    # To do this, we can remove any elements where the second element
    # is not prime or contains a zero.
    return [x for x in pairs if x[1] in primes and not any(x[1] % y == 0 for y in range(2, int(x[1] ** 0.5) + 1))]
