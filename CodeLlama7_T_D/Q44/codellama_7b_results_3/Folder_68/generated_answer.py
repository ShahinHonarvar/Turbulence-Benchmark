
def composite_nums_between_indices(my_list):
    # Create a set to store the composite numbers
    composite_numbers = set()

    # Iterate over the list of positive integers
    for num in my_list:
        # Check if the number is composite by dividing it by 2 and checking if it has any remainders
        if num % 2 != 0:
            # If the number is not divisible by 2, then check if it is divisible by any other odd numbers less than or equal to its square root
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    # If the number is divisible by an odd number less than or equal to its square root, then it is not prime and should be added to the set of composite numbers
                    composite_numbers.add(num)

    return composite_numbers
