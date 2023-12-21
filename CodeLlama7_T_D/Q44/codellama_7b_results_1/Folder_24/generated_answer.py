
def composite_nums_between_indices(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Define the range of indices to consider
    start_index = 34
    end_index = 55
    # Initialize an empty set to store the composite numbers
    composite_numbers = set()

    for i in range(start_index, end_index + 1):
        # Check if the current number is prime or not
        if my_list[i] != 1:
            # If it's not prime, check if it's composite by dividing it by all numbers less than its square root
            for j in range(2, int(my_list[i]) ** 0.5 + 1)):
                if my_list[i] % j == 0:
                    # If the number is divisible by any number less than its square root, it's not composite
                    break
            else:
                # If we reach the end of the loop without breaking, the number is likely composite
                composite_numbers.add(my_list[i])
    return composite_numbers
