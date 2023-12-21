
def all_right_truncatable_prime(tuple_of_numbers):
    # helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # helper function to check if a number is right-truncatable prime
    def is_right_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    # main function
    x = tuple_of_numbers[93]
    result = []

    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)

    return sorted(result)
