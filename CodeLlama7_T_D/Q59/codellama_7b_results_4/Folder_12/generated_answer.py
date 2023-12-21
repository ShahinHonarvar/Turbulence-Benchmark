
def all_left_truncatable_prime(tuple):
    # Initialize an empty list for storing the left-truncatable prime numbers
    left_truncatable_primes = []
     # Loop through each element in the tuple
     for i in range(len(tuple)):
        # Get the current integer element from the tuple
        current_element = tuple[i]
         # Check if the current element is a prime number
        if is_prime(current_element):
             # If the current element is a prime number, append it to the list of left-truncatable prime numbers
            left_truncatable_primes.append(current_element)
         # Loop through each digit in the current integer element from the tuple
        for j in range(len(str(current_element)))):
             # Get the current digit from the string representation of the current integer element from the tuple
            current_digit = str(current_element)[j]
             # Check if the current digit is not equal to 0
            if current_digit != '0':
                 # Remove the current digit from the string representation of the current integer element from the tuple
                new_string = str(current_element).replace(current_digit, '')

                 # Convert the new string back into an integer
                new_integer = int(new_string)

                 # Check if the new integer is a prime number
                if is_prime(new_integer):
                     # If the new integer is a prime number, append it to the list of left-truncatable prime numbers
                    left_truncatable_primes.append(new_integer)

    return sorted(left_truncatable_primes, reverse=True)
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n+1):
        # If n is not divisible by i, it is not prime
        if n % i != 0:
            return False

    # If n is divisible by all numbers less than or equal to its square root, it is prime
    if n <= int(math.sqrt(n)):
        return True

    # If n is greater than its square root, it is not prime
    else:
        return False
