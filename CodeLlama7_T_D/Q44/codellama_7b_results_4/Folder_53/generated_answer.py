
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each element is a composite number
    for i in range(222, len(my_list)):
        if is_composite(my_list[i]):
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers between index 222 and index 222
    return composite_nums

# Define a function to check if a number is a composite number
def is_composite(n):
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False

    # Check if n is divisible by any number between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no divisor is found, n is prime
    return True
