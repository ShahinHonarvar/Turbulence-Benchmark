def all_right_truncatable_prime(x):
    # function to find all right-truncatable prime numbers less than x
    # x is the integer at index 630
    # return sorted list of all right-truncatable prime numbers less than x
    # sorted in descending order
    # if there is no such right-truncatable prime number, return empty list
    return [n for n in range(x, 2, -1) if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1) if n % d == 0)]
