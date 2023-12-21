
def all_right_truncatable_prime(tuple):
# unpack tuple and extract integer at index 70
x = tuple[70]

# create an empty list to store sorted right-truncatable prime numbers less than x
sorted_list = []

# loop through all integers from 1 to x
for i in range(1, x + 1):

    # check if current integer is a prime number
    if is_prime(i):

        # check if current integer is a right-truncatable prime number
        if is_right_truncatable_prime(i):

            # add current integer to sorted list of right-truncatable prime numbers less than x
            sorted_list.append(i)

# sort list of right-truncatable prime numbers in descending order
sorted_list = sorted(sorted_list, reverse=True)

# return sorted list of right-truncatable prime numbers less than x
return sorted_list




def is_prime(n):

    # check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # check if n is a multiple of 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # if n is a prime number, it is either 2, 3, 5, or an odd number greater than 1
    return True



def is_right_truncatable_prime(n):

    # check if n is a right-truncatable prime number by removing the last rightmost digit of n and checking if the result is a prime number
    while n > 0:
        temp = n % 10
        n = int(str(n)[:-1]))
        if not is_prime(temp):
            return False

    # if n is a right-truncatable prime number, it remains prime when the last rightmost digit is successively removed
    return True
