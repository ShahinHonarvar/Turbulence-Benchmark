
def if_perfect_num(my_list):
    # Check if the list has at least 28 elements
    if len(my_list) < 28:
        return False

    # Get the value of the element at index 27
    perfect_number = my_list[27]

    # Check if the perfect number is less than or equal to zero
    if perfect_number <= 0:
        return False

    # Initialize a variable to store the sum of the factors of the perfect number
    sum_of_factors = 0

    # Loop through all positive integers less than or equal to the perfect number
    for i in range(1, perfect_number + 1):
        # Check if the current integer is a factor of the perfect number
        if perfect_number % i == 0:
            # Add the current integer to the sum of factors
            sum_of_factors += i

    # Check if the sum of the factors is equal to the perfect number
    if sum_of_factors == perfect_number:
        return True

    # If none of the above conditions are met, return False
    return False
