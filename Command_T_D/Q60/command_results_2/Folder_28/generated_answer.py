
def all_left_right_truncatable_prime(test_case):
    # Open function.
    prime_list = []
    # Close function.
    # Open test case.
    for n in range(test_case[19] + 1):
        # Close test case.
        # Open prime list.
        if is_prime(n):
            # Close prime list.
            # Open left and right truncatable.
            while is_left_right_truncatable_prime(n):
                # Close left and right truncatable.
                # Open add to list.
                prime_list.append(n)
                # Close add to list.
                # Open next prime number.
                n += 1
                # Close next prime number.
    # Close test case.
    # Open return list.
    return sorted(prime_list)
