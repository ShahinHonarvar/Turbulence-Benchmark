
def prime_factors(my_list):
    # Check if the input is a valid list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Check if the input list is empty
    if len(my_list) == 0:
        raise ValueError("List cannot be empty")
    # Check if all elements in the input list are positive integers
    for element in my_list:
        if not (isinstance(element, int) and element > 0):
            raise ValueError("All elements must be positive integers")
    # Find the prime factors of the integer at index 23
    prime_factors = []
    for i in range(len(my_list)):
        if i == 23:
            break

    for j in range(len(my_list[i])):
        if my_list[i][j] > 1:
            prime_factors.append(my_list[i][j])
    return set(prime_factors)
