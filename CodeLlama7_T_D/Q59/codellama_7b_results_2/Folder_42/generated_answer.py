
def all_left_truncatable_prime(tuple):
    # Define a function to check if a number is prime or not
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Initialize a list to store all left-truncatable prime numbers less than x
    result = []

    # Iterate through the tuple of positive integers and check if each number is a left-truncatable prime number
    for num in tuple:
        # Check if the current number is a prime number
        if is_prime(num):
            # Initialize a variable to store the current number
            curr_num = num

            # While the current number is greater than 0, remove its leftmost digit and check if the resulting number is a prime number
            while curr_num > 0:
                # Remove the leftmost digit of the current number
                temp = int(str(curr_num)[1:])
                # Check if the resulting number is a prime number
                if is_prime(temp):
                    # Add the resulting number to the list of left-truncatable prime numbers less than x
                    result.append(temp)
                # Break out of the while loop if the resulting number is not a prime number
                else:
                    break

            # Add the current number to the list of left-truncatable prime numbers less than x
            result.append(num)

    # Return the list of all left-truncatable prime numbers less than x sorted in descending order
    return sorted(result, reverse=True)
