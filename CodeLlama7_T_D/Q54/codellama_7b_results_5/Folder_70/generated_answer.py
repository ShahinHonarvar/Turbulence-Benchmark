
def all_right_truncatable_prime(n):
    # Define a function to check if a number is prime or not
    def is_prime(num):
        if num == 1 or num % 2 == 0:
            return False

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False

        return True

    # Define a function to check if a number is right-truncatable prime or not
    def is_right_truncatable_prime(num):
        if num == 1:
            return False

        for i in range(len(str(num))) - 1, len(str(num))):
            temp = int(str(num)[:i] + str(num)[i + 1:])
            if not is_prime(temp):
                return False

        return True

    # Return the sorted list of all right-truncatable prime numbers less than n
    result = []

    for i in range(n):

        if is_right_truncatable_prime(i):

            result.append(i)

    return sorted(result, reverse=True)
