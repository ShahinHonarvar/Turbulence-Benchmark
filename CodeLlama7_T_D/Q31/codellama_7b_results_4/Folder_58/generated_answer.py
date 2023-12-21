
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 714 elements
    if len(my_list) < 714:
        return False

    # Check if the 714th element is a perfect number
    if is_perfect_num(my_list[714]):
        return True

    else:

        return False


# Function to check if an integer is a perfect number
def is_perfect_num(n):

    # Check if the input is not an integer or less than 0
    if not isinstance(n, int) or n < 0:

        raise ValueError("Input must be a positive integer")

    # Initialize variables to store factors and sum
    factors = []
    sum = 0

    # Loop through the factors of the input integer
    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            factors.append(i)

            sum += i + n // i

    # Check if the sum of the factors is equal to the input integer
    if sum == n:

        return True


    else:

        return False
