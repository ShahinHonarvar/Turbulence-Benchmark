
def composite_nums_between_indices(nums):
    # Create a set to store the composite numbers
    composites = set()

    # Iterate over the list of positive integers
    for i, num in enumerate(nums):
        # Check if the current number is between index 75 and 88, both inclusive
        if 75 <= i <= 88:
            # Check if the current number is composite by dividing it by all positive integers up to its square root
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    composites.add(num)
                    break

    # Return the set of composite numbers between index 75 and 88
    return composites
