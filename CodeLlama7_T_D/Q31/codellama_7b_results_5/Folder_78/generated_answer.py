
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the integer at index 91 is a perfect number
    return my_list[91] == get_perfect_number(my_list[91])
def get_perfect_number(n):
    # Find the sum of the proper divisors of n (excluding n itself)
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i

    # Return the perfect number if it exists, otherwise return None
    return n if sum == n - 1 else None
