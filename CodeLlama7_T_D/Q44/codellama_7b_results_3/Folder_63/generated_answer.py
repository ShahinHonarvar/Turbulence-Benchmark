
def composite_nums_between_indices(my_list):
    # Define the range of indices to check for compositeness
    start_index = 17
    end_index = 78
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list and check if each element is a prime number
    for i in range(start_index, end_index + 1):
        current_element = my_list[i]
        if is_prime(current_element):
            composite_numbers.add(current_element)

    # Return the set of all composite numbers between the specified indices
    return composite_numbers

# Define a function to check if a number is prime
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
