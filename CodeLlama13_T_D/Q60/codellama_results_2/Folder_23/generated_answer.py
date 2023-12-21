
def all_left_right_truncatable_prime(x):
    # initialize an empty list to store the left-and-right-truncatable prime numbers
    primes = []
    
    # iterate through all positive integers less than or equal to x
    for i in range(2, x + 1):
        # check if the current integer is a prime number
        if is_prime(i):
            # check if the current integer contains no 0
            if '0' not in str(i):
                # check if the current integer remains prime when successively removing leading and trailing digits
                while len(str(i)) > 1:
                    i = int(str(i)[:-1])
                    if not is_prime(i):
                        break
                else:
                    primes.append(i)
    
    # return the list of left-and-right-truncatable prime numbers in descending order
    return sorted(primes, reverse=True)
