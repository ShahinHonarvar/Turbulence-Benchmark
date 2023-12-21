
def all_right_truncatable_prime(tuple_of_positive_integers):
    # Get the integer at index 70 from the tuple
    x = tuple_of_positive_integers[70]
    # Initialize an empty list to store the right-truncatable prime numbers less than x
    list_of_right_truncatable_prime_numbers = []
    # Iterate over all prime numbers less than x
    for i in range(2, x):
        # Check if the current prime number is a right-truncatable prime number
        if is_right_truncatable_prime(i):
            # If the current prime number is a right-truncatable prime number, add it to the list of right-truncatable prime numbers less than x
            list_of_right_truncatable_prime_numbers.append(i)
    # Sort the list of right-truncatable prime numbers in descending order
    list_of_right_truncatable_prime_numbers = sorted(list_of_right_truncatable_prime_numbers, reverse=True)
    return list_of_right_truncatable_prime_numbers
