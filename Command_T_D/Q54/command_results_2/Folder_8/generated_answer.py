def all_right_truncatable_prime(test_case):
    # sort by number of digits
    test_case = sorted(test_case, key=lambda x: int(str(x).rstrip("0")))
    # the last number is always right-truncatable
    last = test_case[-1]
    # the next number that is right-truncatable is the last number minus 1
    next_r_t_p = last - 1
    # for every number in the test case, check if it is right-truncatable
    r_t_p = [next_r_t_p]
    while r_t_p:
        # check if the number is prime
        if is_prime(r_t_p[-1]):
            # check if the number remains prime when the last rightmost digit is removed
            for _ in range(10):
                # remove the last digit
                r_t_p.append(int(str(r_t_p[-1]).rstrip("0") + str(int(str(r_t_p[-1])[0])))
                # check if the number is prime
                if not is_prime(r_t_p[-1]):
                    break
            else:
                # the number is right-truncatable
                r_t_p.append(r_t_p[-1])
        # remove the last number from the list of right-truncatable primes
        r_t_p.pop()
        # find the next right-truncatable prime number
        next_r_t_p = r_t_p[-1] - 1
    return r_t_p
