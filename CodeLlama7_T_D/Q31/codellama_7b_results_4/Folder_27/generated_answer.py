
def if_perfect_num(my_list):
    # Check if the list is empty
    if not my_list:
        return False

    # Check if the element at index 56 exists in the list
    try:
        element = my_list[56]
    except IndexError:
        return False

    # Check if the element is a perfect number
    if not is_perfect_number(element):
        return False

    return True

# Function to check if an integer is a perfect number
def is_perfect_number(n):
    # Calculate the sum of the divisors of n
    sum_of_divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if n / i != i:
                sum_of_divisors += n / i

    # Check if the sum of the divisors is equal to n
    return sum_of_divisors == n
