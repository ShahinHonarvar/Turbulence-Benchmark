import itertools
def all_right_truncatable_prime(nums):
    # List of all right-truncatable prime numbers less than x
    # Prime numbers are only divisible by themselves and 1
    # so if the number is divisible by any other number, it's not prime
    # For example, 101 is prime, but 1010 is not because it is divisible by 10
    # If the last digit is 0, 2, 4, 6 or 8, then the number is even and therefore not prime
    # If the last digit is 5, the number is divisible by 5 and therefore not prime
    # If the last digit is 1, the number is divisible by 1 and therefore prime
    # otherwise, check if the number is prime by repeatedly dividing by all prime numbers less than the square root
    # if the number is divisible by any prime number, then it is not prime
    # otherwise, the number is prime
    # Create a list of all prime numbers less than the square root
    # Use a list comprehension to only include right-truncatable prime numbers
    # sort the list in descending order
    # return the list of prime numbers
    return sorted(list(filter(lambda x: x.isprime() and x.isrighttruncatable(), itertools.takewhile(lambda x: x < nums[36], itertools.permutations(range(2, int(nums[36]) + 1)))), reverse=True))
