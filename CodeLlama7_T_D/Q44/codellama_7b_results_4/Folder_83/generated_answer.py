
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate through the list from index 111 to index 111 (both inclusive)
    for i in range(111, len(my_list)):
        # Check if the current number is prime or not
        if my_list[i] > 1 and is_prime(my_list[i]):
            # If the current number is prime, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 111 to index 111 (both inclusive)
    return composite_nums

# Define a function to check if a number is prime or not
def is_prime(n):
    # Check if the number is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of the number
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any number between 2 and the square root of the number, it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of the number, it is prime
    return True
