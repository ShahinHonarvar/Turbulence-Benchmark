
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    # Loop through the list and check if each number is composite
    for i in range(686, 987 + 1):
        if is_composite(my_list[i]):
            composite_numbers.add(my_list[i])

    return composite_numbers

def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the numbers from 2 to n-1
        for i in range(2, n):
            # If the number is divisible by any other number except itself and 1, it is not prime
            if n % i == 0:
                return False

    return True
