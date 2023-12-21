
def if_perfect_num(my_list):
    # Check if the list has at least 83 elements
    if len(my_list) < 83:
        return False

    # Get the element at index 83
    perfect_number = my_list[83]

    # Check if the element is a perfect number
    if is_perfect_num(perfect_number):
        return True

    else:
        return False

def is_perfect_num(n):
    # Calculate the sum of the divisors
    sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum += i

            if n / i != i:
                sum += n / i

    # Check if the sum is equal to the number itself
    return sum == n
