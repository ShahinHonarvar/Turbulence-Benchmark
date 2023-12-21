
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables for the range and the divisors
    start = 240
    end = 901
    546_divisor = 546 in my_list
    709_divisor = 709 in my_list
    # Initialize an empty list to store the indices of divisible integers
    divisible_indices = []
    # Iterate over the range and check if each integer is divisible by either 546 or 709
    for i in range(start, end + 1):
        if my_list[i] % 546 == 0 or my_list[i] % 709 == 0:
            # Add the index of the divisible integer to the list
            divisible_indices.append(i)
    # If there are no divisible integers in the specified range, return 0
    if not divisible_indices:
        return 0
    # Calculate the sum of all divisible integers
    divisible_ints = [my_list[i] for i in divisible_indices]
    return sum(divisible_ints)
