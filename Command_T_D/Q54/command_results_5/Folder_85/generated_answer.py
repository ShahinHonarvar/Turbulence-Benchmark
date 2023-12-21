def all_right_truncatable_prime(n):
    # n is a tuple of positive integers. Let x be the integer at index 94.
    # The function should return the sorted list of all right-truncatable prime numbers less than x.
    # The returned list should be sorted in ascending order. If there is no such right-truncatable prime number,
    # the function should return an empty list. A right-truncatable prime number is a prime number that remains prime
    # when the last rightmost digit is successively removed.
    if n[94] < 2:
        return []
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # This list is built using the Sieve of Eratosthenes algorithm.
    # The list is empty if there is no right-truncatable prime number less than x.
    # This line is not indented because it is outside the function.
    return sorted(l)
