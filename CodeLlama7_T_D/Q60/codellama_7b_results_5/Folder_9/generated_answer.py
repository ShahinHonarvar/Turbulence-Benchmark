
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # filter the list to include only left-and-right-truncatable prime numbers
    return sorted([p for p in prime_list if str(p)[1:] == str(p)[:-1] and not '0' in str(p)], reverse=True)
