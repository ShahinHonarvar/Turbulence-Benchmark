 def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        # check if i is prime by dividing it only by the first few prime numbers
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # if is_prime is true, add i to the prime_list
        if is_prime:
            prime_list.append(i)

    # create an empty list to store all left-and-right-truncatable prime numbers in the range of x
    lrt_prime_list = []

    # loop through each prime number in the prime_list and check if it is a left-and-right-truncatable prime number
    for i in prime_list:
        # initialize variables to store the leading leftmost and last rightmost digits of the current prime number being checked
        leading_leftmost_digit = 0
        last_rightmost_digit = 0

        # check if the current prime number being checked has no 0s in its representation
        if str(i).count("0") == 0:
            # loop through each digit of the current prime number being checked
            for j in range(len(str(i)))):
                # store the leading leftmost digit of the current prime number being checked
                if leading_leftmost_digit == 0:
                    leading_leftmost_digit = int(str(i))[j]
                # store the last rightmost digit of the current prime number being checked
                last_rightmost_digit = int(str(i))[len(str(i)) - j - 1])

            # check if the leading leftmost and last rightmost digits of the current prime number being checked are both prime numbers themselves
            if isprime(leading_leftmost_digit) and isprime(last_rightmost_digit):
                # add the current prime number to the lrt_prime_list if it is a left-and-right-truncatable prime number
                lrt_prime_list.append(i)

    # sort the lrt_prime_list in ascending order and return it
    return sorted(lrt_prime_list)
