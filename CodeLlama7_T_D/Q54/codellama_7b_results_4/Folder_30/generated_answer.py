
def all_right_truncatable_prime(tuple):
    # Initialize an empty list for storing the prime numbers
    prime_list = []

    # Iterate through the tuple elements
    for i in range(len(tuple)):
        x = tuple[i]
        # Check if x is a prime number
        if is_prime(x):
            # Initialize a variable to store the last rightmost digit of x
            last_digit = x % 10

            # Remove the last rightmost digit from x and check if it remains prime
            while last_digit != 0:
                y = x // 10

                if is_prime(y):
                    # If the number is right-truncatable, add it to the list
                    prime_list.append(x)

                # Remove the last rightmost digit from x and check if it remains prime
                x = y * 10 + last_digit

                # Update the value of last_digit
                last_digit = x % 10

    # Sort the list in descending order
    prime_list.sort(reverse=True)

    return prime_list

def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False

    # Check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
