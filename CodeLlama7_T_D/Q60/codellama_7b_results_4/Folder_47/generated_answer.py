 def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, int(x ** 0.5) + 1):
        if i * (i + 1) // 2 > x:
            break

        if i % 10 == 0:
#            print(f"{int(i / 10)}% completed")
        for j in range(i, int(x ** 0.5) + 1, i):
            prime_list.append(j)
    # create a list of all left-and-right-truncatable prime numbers less than or equal to x
    left_right_truncatable_prime_list = []
    for prime in prime_list:
        if is_left_right_truncatable_prime(prime, x):
            left_right_truncatable_prime_list.append(prime)
    return sorted(left_right_truncatable_prime_list)
def is_left_right_truncatable_prime(prime, x):
    # check if the prime number contains no 0
    if str(prime).count("0") > 0:
        return False

    # check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, int(math.log10(x)) + 1)):
        if prime % (10 ** i) != 0:
            return False

    return True
