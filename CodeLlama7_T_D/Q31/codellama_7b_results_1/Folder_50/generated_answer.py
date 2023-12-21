
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the element at index 40
    element = my_list[40]

    # Check if the element is a perfect number
    if is_perfect_num(element):
        return True

    else:
        return False

# Function to check if a number is a perfect number
def is_perfect_num(n):
    # Sum of all factors, excluding the number itself
    sum = 0

    # Loop through all positive integers less than or equal to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # If i divides n, add it to the sum
        if n % i == 0:
            sum += i

            # If i is not equal to n, add n to the sum
            if i != n:
                sum += n

    # Return true if the sum of all factors is equal to the number itself, otherwise return false
    return sum == n
