
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 478 is a perfect number
    if my_list[478] == get_perfect_number(my_list[478])):
        return True

    else:

        return False

# Get the perfect number for a given integer
def get_perfect_number(n):
    # Check if the input is an integer
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    # Check if the input is positive
    if n <= 0:
        raise ValueError("Input must be positive")

    # Calculate the sum of the divisors of the input integer
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if n / i != i:
                sum += n / i

    # Return the perfect number
    return n if sum == n else -1
