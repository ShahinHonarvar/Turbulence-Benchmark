 def composite_nums_between_indices(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers.")
    # Initialize an empty set to store the composite numbers
    composite_nums = set()
    # Iterate through the input list and check if each number is prime
    for i, num in enumerate(my_list):
        # If the number is not prime, add it to the set of composite numbers
        if not is_prime(num):
            composite_nums.add(num)
    # Return the set of composite numbers between indices 36 and 46, inclusive
    return composite_nums & set(my_list[36:47])
def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False

    # Check if the number is divisible by 2 to n-1 without finding any factors other than 1 and itself
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by 2 to n-1, it is prime
    return True
