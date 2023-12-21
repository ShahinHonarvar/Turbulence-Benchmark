
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is greater than 1
        if my_list[i] > 1:
            # Use the modulo operator to check if the current number is divisible by any number between 2 and the square root of the current number
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    # If the current number is divisible by any number between 2 and the square root of the current number, it is not a prime number
                    break
            else:
                # If the loop completes without finding any divisors, the current number is prime
                composite_nums.add(my_list[i])

    return composite_nums
