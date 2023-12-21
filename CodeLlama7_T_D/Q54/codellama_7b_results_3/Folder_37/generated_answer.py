
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    results = []

    # Loop through each element in the tuple
    for i in range(len(tuple)):
        # Set the current element as the variable x
        x = tuple[i]

        # Check if x is a prime number and add it to the list of results if it is
        if is_prime(x):
            results.append(x)

        # Loop through each digit in the base 10 representation of x
        for j in range(len(str(x)))):
            # Set the current digit as the variable d
            d = int(str(x))[j])

            # Check if removing the rightmost digit from x results in a prime number and add it to the list of results if it is
            if is_prime(int(str(x))))[:-1]):
                results.append(int(str(x))))[:-1]))

    return sorted(results, reverse=True)
