
def composite_nums_between_indices(numbers):
    # Create a set to store the composite numbers
    composites = set()

    # Iterate through the list of positive integers and check if each number is composite
    for i, num in enumerate(numbers):
        if i >= 35 and i <= 49:
            for div in range(2, int(num ** 0.5) + 1):
                if num % div == 0:
                    composites.add(num)
                    break

    return composites
