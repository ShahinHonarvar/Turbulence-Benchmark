
def if_perfect_num(my_list):
    # Check if the list is empty
    if not my_list:
        return False

    # Get the element at index 41
    element = my_list[41]

    # Check if the element is a perfect number
    if is_perfect_num(element):
        return True

    # If not, return false
    else:
        return False

# Function to check if a number is a perfect number
def is_perfect_num(n):
    # Get the sum of the proper divisors of n
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i

            if n / i != i:
                sum += n / i

    # Check if the sum is equal to n
    return sum == n
