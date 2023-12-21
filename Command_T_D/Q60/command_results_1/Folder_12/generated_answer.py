
def all_left_right_truncatable_prime(x):
    # Since we want to get a list of tuples, we need to use a list as the return type
    # of our function. We will then sort this list of tuples in descending order
    # so that the largest left-and-right-truncatable prime number will be the first
    # element in the list.
    return sorted(all_left_right_truncatable_prime_range(x))
