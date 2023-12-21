
def all_right_truncatable_prime(tuple):
    # initialize an empty list to store the prime numbers
    prime_list = []

    # loop through the tuple and check if each number is a right-truncatable prime number
    for num in tuple:
        # check if the number is prime
        if is_prime(num):
            # initialize a variable to store the number of times the last digit has been removed without causing the number to become non-prime
            count = 0

            # loop through the digits of the number in reverse order
            for digit in str(num)[::-1]:
                # check if the number is still prime after removing the last rightmost digit
                if is_prime(int(str(num)[:len(str(num)) - 1] + digit))):
                    # increment the count variable
                    count += 1

            # check if the number has been removed the same number of times as its length in order to be considered a right-truncatable prime number
            if count == len(str(num))):
                # add the number to the list of prime numbers
                prime_list.append(num)

    # sort the list of prime numbers in descending order and return it
    return sorted(prime_list, reverse=True)

# define a function to check if a number is prime
def is_prime(n):
    # check if the number is greater than 1
    if n > 1:
        # loop through all the numbers from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1)):
            # check if any of the numbers divide the number without leaving a remainder
            if n % i == 0:
                # return false if any divisor is found
                return False

    # if the number is less than or equal to 1, it is not prime
    else:
        # return false if the number is less than or equal to 1
        return False

    # if no divisor is found, return true
    return True
