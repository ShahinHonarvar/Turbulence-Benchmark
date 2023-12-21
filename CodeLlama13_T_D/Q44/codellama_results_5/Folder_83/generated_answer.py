
def composite_nums_between_indices(numbers):
    # Initialize an empty set to store the composite numbers
    composites = set()

    # Iterate through the list of positive integers
    for i, num in enumerate(numbers):
        # Check if the current number is between indices 111 and 111 (both inclusive)
        if i >= 110 and i <= 111:
            # Check if the current number is composite
            if any(num % x == 0 for x in range(2, int(num ** 0.5) + 1)):
                # Add the current number to the set of composites
                composites.add(num)

    return composites
