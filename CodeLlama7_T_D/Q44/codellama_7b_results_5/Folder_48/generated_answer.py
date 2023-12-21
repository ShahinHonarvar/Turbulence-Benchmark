
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list from index 661 to 924 (both inclusive)
    for i in range(661, 925):

        # Check if the current number is a prime number using the Sieve of Eratosthenes algorithm
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the current number is a prime number and it is between index 661 to 924 (both inclusive), add it to the set of composite numbers
        if is_prime and 661 <= i <= 924:
            composite_nums.add(i)

    # Return the set of all composite numbers in the given list that are between index 661 to 924 (both inclusive), or an empty set if no composite number exists in the specified range
    return composite_nums
