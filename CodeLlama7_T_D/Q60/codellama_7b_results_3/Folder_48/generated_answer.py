
def all_left_right_truncatable_prime(x):
    # create a list of prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        # check if i is a prime number
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    # create a list of left-and-right-truncatable prime numbers
    left_right_truncatable_prime_list = []
    for i in prime_list:
        # check if i is a left-and-right-truncatable prime number
        if str(i) == str(i)[1:] and str(i) == str(i)[:-1]:
            left_right_truncatable_prime_list.append(i)
    # sort the list of left-and-right-truncatable prime numbers in ascending order
    left_right_truncatable_prime_list.sort()
    return left_right_truncatable_prime_list
