
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list and check if each number is composite
    for i in range(len(my_list)):
        num = my_list[i]
        if is_composite(num):
            composite_nums.add(num)

    # Return the set of all composite numbers between indices 5 and 7, inclusive
    return composite_nums

# Function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the number is divisible by any number between 2 and the square root of n, it is not prime
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and the square root of n, it is prime
    return True
